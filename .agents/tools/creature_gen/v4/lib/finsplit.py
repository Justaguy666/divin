import v4env  # noqa: F401  (paths)
import numpy as np
from scipy import ndimage as ndi
def fin_split(fr,core,L,C,a=None,b=None):
    """fin value vs body by fin: each connected fin outside the body is 'vivid' if its median chroma >= 0.06, else 'clear'"""
    fin=(fr[...,3]>0)&~ndi.binary_dilation(core); lab_,n=ndi.label(fin,structure=np.ones((3,3))); Lb=L[core].mean()
    vv=[];cc=[]
    for i in range(1,n+1):
        m=lab_==i
        if m.sum()<3: continue
        if np.median(C[m])>=0.06:
            if a is not None:
                h=np.degrees(np.arctan2(np.median(b[m]),np.median(a[m])))
                if -35<=h<=75: continue   # red/orange/copper signature fins keep their own depth (a lift turns them salmon); not judged here
            vv.append(m)
        else: cc.append(m)
    f=lambda ms: float(L[np.any(ms,0)].mean()-Lb) if ms and np.any(ms,0).sum()>=5 else np.nan
    return f(cc),f(vv)
if __name__=='__main__':
    import os,sys
    
    from f2 import frames,lab
    from m import body
    for p in v4env.BIOME:
        c_=[];v_=[]
        for n,fr,f in frames(p):
            core=body(fr); L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b); c,v=fin_split(fr,core,L,C)
            if not np.isnan(c): c_.append(c)
            if not np.isnan(v): v_.append(v)
        print(p,'clear fins dL med %+.2f IQR %+.2f %+.2f n=%d | vivid fins dL med %+.2f IQR %+.2f %+.2f n=%d'%(np.median(c_),*np.percentile(c_,[25,75]),len(c_),np.median(v_) if v_ else np.nan,*(np.percentile(v_,[25,75]) if v_ else (np.nan,np.nan)),len(v_)))
