import v4env  # noqa: F401  (paths)
import os,sys,json,numpy as np

from f2 import lab,frames
from m import BI,body
from scipy import ndimage as ndi
def feat3(fr):
    A=fr[...,3]; op=A>=200; core=body(fr)
    if core.sum()<30: return None
    L=lab(fr[...,:3].astype(float))[0]; Lb=L[core]; lo,hi=np.percentile(Lb,2),np.percentile(Lb,98); rng=max(hi-lo,1e-3)
    q=np.clip(((L-lo)/rng*7).astype(int),0,6)
    inner=ndi.binary_erosion(core)
    h=inner[:,1:]&inner[:,:-1]; v=inner[1:]&inner[:-1]
    Hc=(q[:,1:]==q[:,:-1])[h].mean(); Vc=(q[1:]==q[:-1])[v].mean()
    ys,xs=np.nonzero(core); x0,x1=xs.min(),xs.max(); BL=x1-x0+1
    darkthick=[];outl=[];steps=[];cs=[];lightzone=[]
    for x in range(x0+int(BL*.25),x0+int(BL*.75)+1):
        c=np.nonzero(core[:,x])[0]
        if len(c)<8: continue
        vv=L[c,x]; n=len(c); mid=lo+0.5*rng
        k=int(np.argmax(vv[1:-1]))+1
        lower=vv[k:]; darkthick.append(float((lower<mid).sum()/n))
        # outline thickness at the bottom: consecutive rows from bottom below lo+0.2*rng
        t=0
        for val in vv[::-1]:
            if val<lo+0.2*rng: t+=1
            else: break
        outl.append(t)
        # distinct value steps from lightest down to bottom
        qq=q[c[k:],x]; steps.append(int(len(np.unique(qq))))
        # countershading: inner belly (t .7-.9) minus back (t .1-.3)
        tt=np.arange(n)/(n-1); b_=vv[(tt>=.7)&(tt<=.9)]; bk=vv[(tt>=.1)&(tt<=.3)]
        if len(b_) and len(bk): cs.append(float(b_.mean()-bk.mean()))
        lightzone.append(float((vv>=lo+0.7*rng).sum()/n))
    # outline ring completeness: perimeter pixels of opaque silhouette next to core darker than inward neighbour
    pad=np.pad(op,1); edge=op&(~pad[:-2,1:-1]|~pad[2:,1:-1]|~pad[1:-1,:-2]|~pad[1:-1,2:])&ndi.binary_dilation(core)
    cy,cx=ndi.center_of_mass(core); ring=[]
    for y,x in zip(*np.nonzero(edge)):
        dy,dx=np.sign(cy-y),np.sign(cx-x)
        if abs(cy-y)>abs(cx-x)*0.5: dx=0
        else: dy=0
        y2,x2=int(y+dy),int(x+dx)
        if op[y2,x2]: ring.append(L[y,x]<L[y2,x2]-0.06)
    # eye dominance: pupil = darkest pixel in front 35% with a pixel >=0.3 lighter right above
    U=(np.arange(fr.shape[1])-x0)/max(BL-1,1); front=core&(U[None,:]>0.65)
    cand=[(L[y,x],y,x) for y,x in zip(*np.nonzero(front)) if y>0 and L[y-1,x]-L[y,x]>0.3]
    if cand:
        lp,py,px=min(cand); head=front.copy(); head[py,px]=False
        eyedom=float((L[head]<=lp+0.04).mean()); pupil=float(lp)
    else: eyedom=np.nan; pupil=np.nan
    return dict(Hc=float(Hc),Vc=float(Vc),HV=float(Hc/max(Vc,1e-3)),darkthick=float(np.median(darkthick)),outl=float(np.median(outl)),
                steps=float(np.median(steps)),cshade=float(np.median(cs)),lightzone=float(np.median(lightzone)),ring=float(np.mean(ring)) if ring else np.nan,eyedom=eyedom,pupil=pupil)
if __name__=='__main__':
    res={}
    for p in BI:
        res[p]={}
        for n,fr,f in frames(p):
            r=feat3(fr)
            if r: res[p][n]=r
    json.dump(res,open('f3.json','w'))
    order=list(BI)
    K=list(next(iter(res['ac'].values())).keys())
    print('%-10s'%'feat'+''.join('%7s'%p for p in order))
    for k in K:
        vals=[np.nanmedian([r[k] for r in res[p].values()]) for p in order]
        print('%-10s'%k+''.join('%7.3f'%v for v in vals))
    print('eye found share',[round(np.mean([not np.isnan(r['eyedom']) for r in res[p].values()]),2) for p in order])
