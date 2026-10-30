import v4env  # noqa: F401  (paths)
"""Per fin group: how it moves over the 4-frame cycle (A B C D, A=C).  For each group: centroid offset in B and D from A,
the main axis, B/D symmetry, where on the fin the change happens (base half vs tip half), and phase relation between groups."""
import sys,glob,re,json,numpy as np
from scipy import ndimage as ndi
from finstudy import load,groups
from m import body
def sig(f):
    frs,W,H=load(f); C=[]; masks=[]
    for k in range(4):
        core=body(frs[k]); G=groups(frs[k],core)[0]; masks.append((core,G))
        C.append({g:(np.array(np.nonzero(m)[::-1]).mean(1) if m.sum()>=4 else None) for g,m in G.items()})
    out={}
    for g in ('caudal','dorsal','ventral'):
        if any(C[k][g] is None for k in range(4)): continue
        dB=C[1][g]-C[0][g]; dD=C[3][g]-C[0][g]
        ax=int(np.argmax(np.abs(dB)+np.abs(dD)))   # 0 = x (fore-aft), 1 = y (up-down)
        sym=float(np.dot(dB,dD)/(np.linalg.norm(dB)*np.linalg.norm(dD)+1e-9))   # -1: B and D opposite (swing), +1 same side (pulse)
        # where the change happens: pixels of this group in A that change in B, split by distance from the body
        core,Gm=masks[0]; m=Gm[g]; d=ndi.distance_transform_edt(~core); dm=d[m]; med=np.median(dm)
        ch=(np.abs(frs[1].astype(int)-frs[0].astype(int)).sum(-1)>0)
        base=m&(d<=med); tip=m&(d>med)
        out[g]=dict(dBx=float(dB[0]),dBy=float(dB[1]),axis='x' if ax==0 else 'y',sym=sym,mag=float(np.linalg.norm(dB)+np.linalg.norm(dD))/2,
                    base_change=float(ch[base].mean()) if base.sum() else np.nan,tip_change=float(ch[tip].mean()) if tip.sum() else np.nan)
    return out
