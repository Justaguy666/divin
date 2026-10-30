import v4env  # noqa: F401  (paths)
import sys,glob,re,json,numpy as np

from scipy import ndimage as ndi
from m import body
from f2 import lab
from PIL import Image
def colT(core):
    T=np.full(core.shape,np.nan); 
    for x in np.nonzero(core.any(0))[0]:
        c=np.nonzero(core[:,x])[0]; T[c,x]=(c-c.min())/max(c.max()-c.min(),1)
    return T
def hl(f):
    W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',f).groups()); fr=np.array(Image.open(f).convert('RGBA'))[:H,:W]; core=body(fr)
    L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b); T=colT(core); Lc=L[core]
    top=core&(L>=np.percentile(Lc,90)); ring=ndi.binary_dilation(top,iterations=1)&core&~top
    ring2=ndi.binary_dilation(top,iterations=2)&core&~top
    ys,xs=np.nonzero(core); BL=xs.max()-xs.min()+1; BH=ys.max()-ys.min()+1; U=(np.arange(W)[None,:]-xs.min())/BL+0*L
    o=dict(step_ring=float(np.median(L[top])-np.median(L[ring])) if ring.sum() else np.nan,
           step_ring2=float(np.median(L[top])-np.median(L[ring2])) if ring2.sum() else np.nan,
           top_minus_body=float(np.median(L[top])-np.median(Lc)),
           top_C_ratio=float(np.median(C[top])/max(np.median(C[core]),1e-3)),
           top_t=float(np.nanmean(T[top])),top_u=float(U[top].mean()),
           back=float(np.nanmedian(L[core&(T>0.04)&(T<0.22)&(U>0.3)&(U<0.75)])-np.median(Lc)),
           upper=float(np.nanmedian(L[core&(T>=0.22)&(T<0.45)&(U>0.3)&(U<0.75)])-np.median(Lc)),
           mid=float(np.nanmedian(L[core&(T>=0.45)&(T<0.7)&(U>0.3)&(U<0.75)])-np.median(Lc)),
           aspect=BL/BH)
    # brightest major tone vs next major tone (major = >=3% of body)
    P=fr[...,:3][core]; cols,cnt=np.unique(P,axis=0,return_counts=True); cL=lab(cols.astype(float))[0]; maj=cL[cnt>=0.03*core.sum()]
    maj=np.sort(maj)[::-1]; o['major_top_step']=float(maj[0]-maj[1]) if len(maj)>1 else np.nan
    return o
