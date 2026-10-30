import v4env  # noqa: F401  (paths)
"""Structural features of a swimmer sprite (row E, frame 0)."""
import os,re,glob,json,sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

from m import BI,R,body
def lab(rgb):
    c=rgb/255.; c=np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)
    l=0.4122214708*c[...,0]+0.5363325363*c[...,1]+0.0514459929*c[...,2]
    m=0.2119034982*c[...,0]+0.6806995451*c[...,1]+0.1073969566*c[...,2]
    s=0.0883024619*c[...,0]+0.2817188376*c[...,1]+0.6299787005*c[...,2]
    l,m,s=np.cbrt(l),np.cbrt(m),np.cbrt(s)
    return (0.2104542553*l+0.793617785*m-0.0040720468*s,1.9779984951*l-2.428592205*m+0.4505937099*s,0.0259040371*l+0.7827717662*m-0.8086757660*s)
def chue(a,b,w=None):
    if w is None: w=np.ones_like(a)
    return float(np.degrees(np.arctan2((b*w).sum(),(a*w).sum())))
def hd(x,y): return float((x-y+180)%360-180)
def frames(pre):
    for f in sorted(glob.glob(f'{R}/{BI[pre]}/{pre}_*_swim_*_4f.png')):
        mm=re.search(r'_swim_(\d+)x(\d+)_4f',f); W,H=int(mm[1]),int(mm[2])
        im=np.array(Image.open(f).convert('RGBA'))
        yield os.path.basename(f)[len(pre)+1:].split('_swim_')[0],im[:H,:W],f
def feat(fr):
    A=fr[...,3]; op=A>=200; vis=A>0; core=body(fr)
    if core.sum()<30: return None
    L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b)
    ys,xs=np.nonzero(core); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); BL=x1-x0+1; BH=y1-y0+1
    out=dict(BL=int(BL),BH=int(BH),area=int(core.sum()))
    # ---- A. tone ramp
    P=fr[...,:3][core]; cols,inv,cnt=np.unique(P.reshape(-1,3),axis=0,return_inverse=True,return_counts=True)
    cL=lab(cols.astype(float))[0]; o=np.argsort(cL); lv=[]; 
    for i in o:
        if cnt[i]<2: continue
        if lv and cL[i]-lv[-1][0]<0.02: lv[-1][1]+=cnt[i]
        else: lv.append([cL[i],cnt[i]])
    levels=np.array([v[0] for v in lv]); steps=np.diff(levels) if len(levels)>1 else np.array([0])
    out.update(ncol_body=int(len(cols)),levels=int(len(levels)),step_med=float(np.median(steps)),step_max=float(steps.max()),
               top3=float(np.sort(cnt)[::-1][:3].sum()/cnt.sum()),singletons=float((cnt==1).sum()/len(cnt)))
    # ---- B. columns
    runs=[];trans=[];runfrac=[];dpos=[];lpos=[];rim=[];darkstart=[]
    for x in range(x0+int(BL*.25),x0+int(BL*.75)+1):
        c=np.nonzero(core[:,x])[0]
        if len(c)<8: continue
        col=fr[c,x,:3].astype(int); v=L[c,x]; n=len(c)
        ch=np.any(col[1:]!=col[:-1],axis=1); nr=1+ch.sum(); runs.append(nr); runfrac.append(1/nr)
        trans.append(int((np.abs(np.diff(v))>0.04).sum()))
        inner=v[1:-1]; t=(np.arange(1,n-1))/(n-1)
        dpos.append(float(t[np.argmin(inner)])); lpos.append(float(t[np.argmax(inner)]))
        rim.append(float(v[-2]-v[-3]) if n>=4 else 0)
        # where value falls below (max - 50% of range) going down from the lightest pixel
        k=np.argmax(inner); thr=inner.max()-0.5*(inner.max()-inner.min()); below=np.nonzero(inner[k:]<thr)[0]
        darkstart.append(float(t[k+below[0]]) if len(below) else 1.0)
    out.update(runs=float(np.mean(runs)),trans=float(np.mean(trans)),darkpos=float(np.median(dpos)),litpos=float(np.median(lpos)),
               rim=float(np.median(rim)),darkstart=float(np.median(darkstart)),runlen=float(np.mean([BH/r for r in runs])))
    # ---- C. length profile (10 bins tail->head)
    U=(np.arange(fr.shape[1])-x0)/max(BL-1,1); prof=[]
    for i in range(10):
        msk=core&(U[None,:]>=i/10)&(U[None,:]<(i+1)/10)
        prof.append(float(L[msk].mean()) if msk.any() else np.nan)
    prof=np.array(prof); out['lenprof']=(prof-np.nanmean(prof)).tolist()
    # ---- D. highlight
    Lb=L[core]; th=np.percentile(Lb,90); hm=core&(L>=th); hy,hx=np.nonzero(hm)
    T=np.full(L.shape,np.nan); 
    topd=[]
    for x in range(x0,x1+1):
        c=np.nonzero(core[:,x])[0]
        if len(c)<4: continue
        T[c,x]=(c-c.min())/max(c.max()-c.min(),1)
        hc=np.nonzero(hm[c,x])[0]
        if len(hc): topd.append(hc.min())
    lab_,ncomp=ndi.label(hm,structure=np.ones((3,3)))
    sizes=ndi.sum(hm,lab_,range(1,ncomp+1)) if ncomp else [0]
    out.update(hl_u=float(((hx-x0)/BL).mean()),hl_t=float(np.nanmean(T[hm])),hl_topd=float(np.median(topd)) if topd else 0,
               hl_comp=int(ncomp),hl_main=float(max(sizes)/hm.sum()),hl_len=float((hx.max()-hx.min()+1)/BL),hl_thick=float(hm.sum()/max(len(np.unique(hx)),1)))
    # ---- E. outline by side (opaque silhouette edges)
    pad=np.pad(op,1); up=~pad[:-2,1:-1]&op; dn=~pad[2:,1:-1]&op; lf=~pad[1:-1,:-2]&op; rt=~pad[1:-1,2:]&op
    res={}
    for nm,m_,dy,dx in (('top',up&~dn,1,0),('bot',dn&~up,-1,0)):
        yy,xx=np.nonzero(m_&core|m_&ndi.binary_dilation(core))
        d=[];dh=[];cr=[]
        for y,x in zip(yy,xx):
            y2,x2=y+dy,x+dx
            if 0<=y2<L.shape[0] and op[y2,x2]:
                d.append(L[y,x]-L[y2,x2]); 
                if C[y2,x2]>0.02 and C[y,x]>0.01: dh.append(abs(hd(np.degrees(np.arctan2(b[y,x],a[y,x])),np.degrees(np.arctan2(b[y2,x2],a[y2,x2])))))
                cr.append(C[y,x]/max(C[y2,x2],1e-3))
        res[nm]=(float(np.median(d)) if d else 0,float(np.median(dh)) if dh else 0,float(np.median(cr)) if cr else 0)
    edge=op&(up|dn|lf|rt)
    out.update(ol_top=res['top'][0],ol_bot=res['bot'][0],ol_hue_top=res['top'][1],ol_hue_bot=res['bot'][1],ol_cr_bot=res['bot'][2],
               ol_L=float(np.median(L[edge&ndi.binary_dilation(core)])) if (edge&ndi.binary_dilation(core)).any() else 0)
    # ---- F. markings: horizontal residual inside core (shading is mostly vertical)
    inner=ndi.binary_erosion(core)
    Lp=np.where(core,L,np.nan); 
    win=np.stack([np.roll(Lp,s,axis=1) for s in (-2,-1,0,1,2)],0)
    med=np.nanmedian(win,0); r=np.where(inner,L-med,0)
    mk=inner&(np.abs(r)>0.06)
    out['mark_share']=float(mk.sum()/max(inner.sum(),1)); out['mark_dark']=float(((r<-0.06)&inner).sum()/max(mk.sum(),1))
    ml,nm_=ndi.label(mk,structure=np.ones((3,3)))
    if nm_:
        sz=np.array(ndi.sum(mk,ml,range(1,nm_+1))); out['mark_n']=int(nm_); out['mark_1px']=float((sz==1).mean()); out['mark_big']=float((sz>=5).mean()); out['mark_size']=float(np.median(sz))
        cy=np.array(ndi.center_of_mass(mk,ml,range(1,nm_+1)))
        if nm_>=3:
            dd=np.sqrt(((cy[:,None,:]-cy[None,:,:])**2).sum(-1)); np.fill_diagonal(dd,1e9); nn=dd.min(1); out['mark_nncv']=float(nn.std()/nn.mean())
        else: out['mark_nncv']=np.nan
        tt=np.array([np.nanmean(T[ml==i+1]) for i in range(nm_)]); out['mark_t']=float(np.nanmedian(tt))
        # elongation of marks (horizontal vs vertical extent)
        sl=ndi.find_objects(ml); el=[(s[1].stop-s[1].start)/(s[0].stop-s[0].start) for s in sl]; out['mark_hv']=float(np.median(el))
    else: out.update(mark_n=0,mark_1px=np.nan,mark_big=np.nan,mark_size=np.nan,mark_nncv=np.nan,mark_t=np.nan,mark_hv=np.nan)
    # vertical residual too (for stacked stripes): count of within-column reversals handled in trans
    # ---- G. colour by tone
    w=C[core]; La=L[core]; aa=a[core]; bb=b[core]; p25,p75=np.percentile(La,[25,75])
    g={}
    for nm,msk in (('dk',La<=p25),('md',(La>p25)&(La<p75)),('lt',La>=p75)):
        g[nm]=(chue(aa[msk],bb[msk]),float(np.median(w[msk])))
    out.update(h_dk=g['dk'][0],h_md=g['md'][0],h_lt=g['lt'][0],c_dk=g['dk'][1],c_md=g['md'][1],c_lt=g['lt'][1],
               hshift_dk=hd(g['dk'][0],g['md'][0]),hshift_lt=hd(g['lt'][0],g['md'][0]),hue_body=chue(aa,bb,w),c_body=float(np.median(w)),
               chroma_p90=float(np.percentile(w,90)),Lmean=float(La.mean()),Lp5=float(np.percentile(La,5)),Lp95=float(np.percentile(La,95)))
    # ---- H. silhouette
    dep=np.array([core[:,x].sum() for x in range(x0,x1+1)]); uu=np.linspace(0,1,len(dep))
    topc=np.array([np.nonzero(core[:,x])[0].min() if core[:,x].any() else np.nan for x in range(x0,x1+1)])
    botc=np.array([np.nonzero(core[:,x])[0].max() if core[:,x].any() else np.nan for x in range(x0,x1+1)])
    km=int(np.argmax(dep)); mid=(y0+y1)/2
    out.update(maxdep_u=float(uu[km]),pedunc=float(dep[uu<0.3].min()/dep.max()) if (uu<0.3).any() else np.nan,
               back_belly=float((mid-topc[km])/max(botc[km]-mid,0.5)),
               curv_top=float(np.nanmean(np.abs(np.diff(topc,2)))),curv_bot=float(np.nanmean(np.abs(np.diff(botc,2)))))
    # ---- I. fins (semi-transparent + opaque outside core)
    fin=vis&~ndi.binary_dilation(core,iterations=1)
    if fin.sum()>5:
        al=A[fin]; out.update(fin_share=float(fin.sum()/vis.sum()),fin_alpha_med=float(np.median(al)),fin_alpha_lv=int(len(np.unique(al//8))),
                               fin_dL=float(L[fin].mean()-La.mean()),fin_dh=abs(hd(chue(a[fin],b[fin],C[fin]),out['hue_body'])) if C[fin].mean()>0.015 else 0.0,
                               fin_cr=float(np.median(C[fin])/max(out['c_body'],1e-3)))
    else: out.update(fin_share=0,fin_alpha_med=np.nan,fin_alpha_lv=0,fin_dL=np.nan,fin_dh=np.nan,fin_cr=np.nan)
    # ---- J. eye: darkest pixel in front 30% of body with a lighter pixel directly above
    fr_=core&(U[None,:]>0.7); eyok=0; ectr=np.nan
    if fr_.any():
        yy,xx=np.nonzero(fr_); k=np.argmin(L[yy,xx]); ey,ex=yy[k],xx[k]
        if ey>0: eyok=int(L[ey-1,ex]-L[ey,ex]>0.3)
        nb=L[max(ey-2,0):ey+3,max(ex-2,0):ex+3]; ectr=float(np.median(nb)-L[ey,ex])
    out.update(eye_hl=eyok,eye_ctr=ectr)
    # ---- K. cleanliness: orphan pixels (colour differs from all 8 neighbours) in the interior
    Pp=fr[...,:3].astype(int); same=np.zeros(L.shape,int)
    for dy in (-1,0,1):
        for dx in (-1,0,1):
            if dy==0 and dx==0: continue
            same+=np.all(np.roll(np.roll(Pp,dy,0),dx,1)==Pp,axis=-1)
    out['orphans']=float(((same==0)&inner).sum()/max(inner.sum(),1))
    return out
if __name__=='__main__':
    res={}
    for p in BI:
        res[p]={}
        for n,fr,f in frames(p):
            try:
                r=feat(fr)
            except Exception as e:
                print('ERR',p,n,e); r=None
            if r: res[p][n]=r
        print(p,len(res[p]),flush=True)
    json.dump(res,open(os.path.join(v4env.CACHE,'f2.json'),'w'))
