import v4env  # noqa: F401  (paths)
import os,sys,numpy as np

from f2 import lab
from m import body
def lp255(fr):
    """length light profile on fully opaque body pixels only (fins over or beside the body excluded where translucent)"""
    c0=body(fr); core=c0&(fr[...,3]==255)
    if core.sum()<0.5*c0.sum(): core=c0
    L=lab(fr[...,:3].astype(float))[0]; ys,xs=np.nonzero(core); x0,x1=xs.min(),xs.max(); BL=x1-x0+1
    U=(np.arange(fr.shape[1])-x0)/max(BL-1,1); prof=[]
    for i in range(10):
        m=core&(U[None,:]>=i/10)&(U[None,:]<(i+1)/10); prof.append(L[m].mean() if m.any() else np.nan)
    prof=np.array(prof); return float((np.nanargmax(prof[1:-1])+1.5)/10), prof-np.nanmean(prof)
if __name__=='__main__':
    from f2 import frames
    import glob
    from PIL import Image
    for p in ['ac','bw','pf','cs','fs','ms']:
        pk=[];P=[]
        for n,fr,f in frames(p):
            a,b=lp255(fr); pk.append(a); P.append(b)
        pk=np.array(pk); print(p,'lp_peak median %.2f share in [0.55,0.85] %.2f'%(np.median(pk),((pk>=0.55)&(pk<=0.85)).mean()),np.round(np.nanmedian(np.array(P),0),3))
    for t in ['A','i17']:
        pass
