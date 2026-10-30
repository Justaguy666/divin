import v4env  # noqa: F401  (paths)
import sys,glob,re,json,numpy as np
from scipy import ndimage as ndi
from finstudy import load,groups
from m import body
from f2 import lab
def rim(f):
    frs,W,H=load(f); fr=frs[0]; core=body(fr); G=groups(fr,core)[0]; L,a,b=lab(fr[...,:3].astype(float)); A=fr[...,3]
    edge_all=(A>0)&~ndi.binary_erosion(A>0); out={}
    for g,m in G.items():
        if m.sum()<8: continue
        e=m&edge_all; i=m&~edge_all
        if e.sum()<3 or i.sum()<3: continue
        ce=np.array([np.median(L[e]),np.median(a[e]),np.median(b[e])]); ci=np.array([np.median(L[i]),np.median(a[i]),np.median(b[i])])
        # interior mottle: share of interior pixels that differ from both horizontal and vertical neighbours by >0.04 (not part of a line)
        Li=np.where(i,L,np.nan); dx=np.abs(Li-np.roll(Li,1,1)); dy=np.abs(Li-np.roll(Li,1,0))
        mott=np.nanmean(((dx>0.04)&(dy>0.04))[i])
        out[g]=dict(rim_dE=float(np.linalg.norm(ce-ci)),rim_absdL=float(abs(ce[0]-ci[0])),rim_dC=float(np.hypot(*ce[1:])-np.hypot(*ci[1:])),mottle=float(mott),inner_Lstd=float(np.std(L[i])))
    return out
