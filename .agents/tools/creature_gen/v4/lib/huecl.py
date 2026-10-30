import v4env  # noqa: F401  (paths)
import numpy as np
from f2 import lab
from m import body
def ad(x,y): return abs((x-y+180)%360-180)
def hue_cluster(fr):
    """hue drift inside the dominant hue family of the body: lights vs mids and darks vs mids (toward / away from yellow 100 deg), chroma ratios"""
    core=body(fr); L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b); h=np.degrees(np.arctan2(b,a))
    m=core&(C>=0.02)
    if m.sum()<15: return None
    hh=h[m]; best=None
    for c in range(0,360,5):
        n=(np.abs((hh-c+180)%360-180)<=25).sum()
        if best is None or n>best[1]: best=(c,n)
    fam=core&(np.abs((h-best[0]+180)%360-180)<=35)&(C>=0.012)   # pixels of the dominant hue family (greys excluded)
    Lf=L[fam]; af=a[fam]; bf=b[fam]; Cf=C[fam]
    if len(Lf)<15: return None
    p25,p75=np.percentile(Lf,[25,75])
    def hue(msk):
        w=Cf[msk]; return float(np.degrees(np.arctan2((bf[msk]*w).sum(),(af[msk]*w).sum())))
    dk,md,lt=Lf<=p25,(Lf>p25)&(Lf<p75),Lf>=p75
    if min(dk.sum(),md.sum(),lt.sum())<3: return None
    hd_,hm,hl=hue(dk),hue(md),hue(lt)
    return dict(fam_hue=best[0],hue_lt=-(ad(hl,100)-ad(hm,100)),hue_dk=ad(hd_,100)-ad(hm,100),
                cmid=float(np.median(Cf[md])),clt=float(np.median(Cf[lt])/max(np.median(Cf[md]),1e-3)),cdk=float(np.median(Cf[dk])/max(np.median(Cf[md]),1e-3)))
if __name__=='__main__':
    import sys,os
    
    from f2 import frames
    for p in v4env.BIOME:
        R=[hue_cluster(fr) for n,fr,f in frames(p)]; R=[r for r in R if r]
        g=lambda k: np.array([r[k] for r in R])
        print('%s n=%2d hue_lt med %+5.1f IQR [%+5.1f %+5.1f] share>2 %.2f | hue_dk med %+5.1f IQR [%+5.1f %+5.1f] | clt %.2f [%.2f %.2f] | cdk %.2f [%.2f %.2f]'%(p,len(R),np.median(g('hue_lt')),*np.percentile(g('hue_lt'),[25,75]),(g('hue_lt')>2).mean(),np.median(g('hue_dk')),*np.percentile(g('hue_dk'),[25,75]),np.median(g('clt')),*np.percentile(g('clt'),[25,75]),np.median(g('cdk')),*np.percentile(g('cdk'),[25,75])))
