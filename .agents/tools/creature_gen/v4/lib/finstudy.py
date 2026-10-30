import v4env  # noqa: F401  (paths)
"""Fin study: per fin group (caudal / dorsal / ventral) colour, alpha, rays, rim, base-to-edge shading, size, motion."""
import sys,glob,re,json,math,numpy as np

from scipy import ndimage as ndi
from scipy.stats import spearmanr
from m import body
from f2 import lab
from PIL import Image
def load(f):
    im=np.array(Image.open(f).convert('RGBA')); W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',f).groups())
    return [im[0:H,k*W:(k+1)*W] for k in range(4)],W,H
def groups(fr,core):
    A=fr[...,3]; vis=A>0; fin=vis&~core
    ys,xs=np.nonzero(core); x0,x1=xs.min(),xs.max(); H,W=core.shape
    top=np.full(W,H); bot=np.full(W,-1)
    for x in range(x0,x1+1):
        c=np.nonzero(core[:,x])[0]
        if len(c): top[x]=c.min(); bot[x]=c.max()
    X=np.arange(W)[None,:]+0*A; Y=np.arange(H)[:,None]+0*A
    caud=fin&(X<x0)
    inx=(X>=x0)&(X<=x1); tt=top[np.clip(X,0,W-1)]; bb=bot[np.clip(X,0,W-1)]
    dors=fin&inx&(Y<tt); vent=fin&inx&(Y>bb)
    return dict(caudal=caud,dorsal=dors,ventral=vent),x0,x1,top,bot
def circ(h,w):
    z=(w*np.exp(1j*np.radians(h))).sum(); return math.degrees(math.atan2(z.imag,z.real))
def gstats(fr,core,g,kind,BL,BH,L,C,h,bodyL,bodyC,bodyH):
    A=fr[...,3].astype(float); n=g.sum(); o={}
    if n<6: return None
    o['area_rel']=n/core.sum()
    a=A[g]; o['a_med']=np.median(a); o['a_p10']=np.percentile(a,10); o['a_p90']=np.percentile(a,90); o['a_levels']=len(np.unique(a)); o['a_opaque']=(a>=250).mean()
    d=ndi.distance_transform_edt(~core); dg=d[g]; dn=dg/max(dg.max(),1)
    o['a_vs_dist']=spearmanr(dn,a).correlation if np.ptp(a)>0 and np.ptp(dn)>0 else 0.0
    base=g&(d<=1.5); o['a_base']=np.median(A[base]) if base.sum() else np.nan
    edge=g&~ndi.binary_erosion(fr[...,3]>0)   # fin pixels touching transparency
    inner=g&~edge
    o['a_edge']=np.median(A[edge]) if edge.sum() else np.nan; o['a_inner']=np.median(A[inner]) if inner.sum() else np.nan
    o['L_rel']=np.median(L[g])-bodyL; o['C_ratio']=np.median(C[g])/max(bodyC,0.01)
    ch=g&(C>=0.03); o['hue_diff']=abs(((circ(h[ch],C[ch])-bodyH+180)%360)-180) if ch.sum()>3 and bodyH is not None else 0.0
    o['vivid']=(C[g]>0.08).mean(); o['ncol']=len(np.unique(fr[...,:3][g],axis=0))
    o['L_vs_dist']=spearmanr(dn,L[g]).correlation if np.ptp(L[g])>0 else 0.0
    o['rim_dL']=(np.median(L[edge])-np.median(L[inner])) if edge.sum() and inner.sum() else np.nan
    o['rim_dA']=(o['a_edge']-o['a_inner']) if edge.sum() and inner.sum() else np.nan
    # texture: neighbour differences inside the fin; rays run roughly along x for the caudal, along y for dorsal/ventral
    hx=g[:,1:]&g[:,:-1]; vy=g[1:]&g[:-1]
    dLx=np.abs(np.diff(L,axis=1))[hx]; dLy=np.abs(np.diff(L,axis=0))[vy]; dAx=np.abs(np.diff(A,axis=1))[hx]; dAy=np.abs(np.diff(A,axis=0))[vy]
    along,across=(dLx,dLy) if kind=='caudal' else (dLy,dLx); aal,aac=(dAx,dAy) if kind=='caudal' else (dAy,dAx)
    o['tex_L']=np.concatenate([dLx,dLy]).mean() if len(dLx)+len(dLy) else 0.0
    o['ray_aniso_L']=(across.mean()+1e-3)/(along.mean()+1e-3) if len(along) and len(across) else 1.0
    o['tex_A']=np.concatenate([dAx,dAy]).mean() if len(dAx)+len(dAy) else 0.0
    o['ray_aniso_A']=(aac.mean()+0.5)/(aal.mean()+0.5) if len(aal) and len(aac) else 1.0
    med=np.median(L[g]); o['marks']=(np.abs(L[g]-med)>0.10).mean()
    ys,xs=np.nonzero(g)
    o['ext']=( (xs.max()-xs.min()+1)/BL if kind=='caudal' else (ys.max()-ys.min()+1)/BH )
    return o
def motion(frs,kind):
    out=[]
    for k in range(4):
        fr=frs[k]; core=body(fr); G=groups(fr,core)[0][kind]
        ys,xs=np.nonzero(G); out.append((xs.mean(),ys.mean(),G.sum(),xs.min() if len(xs) else np.nan,ys.min() if len(ys) else np.nan,ys.max() if len(ys) else np.nan) if G.sum() else (np.nan,)*6)
    out=np.array(out); o={}
    o['m_cx']=np.nanmax(out[:,0])-np.nanmin(out[:,0]); o['m_cy']=np.nanmax(out[:,1])-np.nanmin(out[:,1]); o['m_area']=(np.nanmax(out[:,2])-np.nanmin(out[:,2]))/max(np.nanmean(out[:,2]),1)
    o['m_tipx']=np.nanmax(out[:,3])-np.nanmin(out[:,3]); o['m_top']=np.nanmax(out[:,4])-np.nanmin(out[:,4]); o['m_bot']=np.nanmax(out[:,5])-np.nanmin(out[:,5])
    ch=[]
    for k in range(1,4):
        a,b=frs[k-1],frs[k]; d=(np.abs(a.astype(int)-b.astype(int)).sum(-1)>0)
        c0=body(a); G=groups(a,c0)[0][kind]; ch.append(d[G].mean() if G.sum() else np.nan)
    o['m_change']=np.nanmean(ch)
    return o
def study(f):
    frs,W,H=load(f); fr=frs[0]; core=body(fr); L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b); h=np.degrees(np.arctan2(b,a))
    G,x0,x1,top,bot=groups(fr,core); ys,xs=np.nonzero(core); BL=x1-x0+1; BH=ys.max()-ys.min()+1
    bodyL=np.median(L[core]); bodyC=np.median(C[core]); ch=core&(C>=0.03); bodyH=circ(h[ch],C[ch]) if ch.sum()>3 else None
    res={}
    for kind,g in G.items():
        s=gstats(fr,core,g,kind,BL,BH,L,C,h,bodyL,bodyC,bodyH)
        if s: s.update(motion(frs,kind)); res[kind]=s
    bc=[]
    for k in range(1,4):
        a_,b_=frs[k-1],frs[k]; d=(np.abs(a_.astype(int)-b_.astype(int)).sum(-1)>0); bc.append(d[body(a_)].mean())
    res['body_change']=float(np.mean(bc)); res['BL']=int(BL); res['aspect']=BL/BH
    return res
