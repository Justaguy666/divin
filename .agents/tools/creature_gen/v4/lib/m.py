import v4env  # noqa: F401  (paths)
import os,re,glob,sys,json
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
R=v4env.CREATURES
BI=dict(v4env.BIOME)   # biome registry (biomes.py)
def oklab_L(rgb):
    c=rgb/255.; c=np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)
    l=0.4122214708*c[...,0]+0.5363325363*c[...,1]+0.0514459929*c[...,2]
    m=0.2119034982*c[...,0]+0.6806995451*c[...,1]+0.1073969566*c[...,2]
    s=0.0883024619*c[...,0]+0.2817188376*c[...,1]+0.6299787005*c[...,2]
    return 0.2104542553*np.cbrt(l)+0.793617785*np.cbrt(m)-0.0040720468*np.cbrt(s)
def load(pre):
    out=[]
    for f in sorted(glob.glob(f'{R}/{BI[pre]}/{pre}_*_swim_*_4f.png')):
        m=re.search(r'_swim_(\d+)x(\d+)_4f',f); W,H=int(m[1]),int(m[2])
        im=np.array(Image.open(f).convert('RGBA'))
        fr=im[0:H,0:W]   # row0 (E), frame 0
        out.append((os.path.basename(f)[len(pre)+1:].split('_swim_')[0],pre,fr,f))
    return out
def body(fr):
    a=fr[...,3]; op=a>=250
    core=ndi.binary_opening(op,structure=ndi.generate_binary_structure(2,1),iterations=2)
    if core.sum()<20: core=op
    lab,n=ndi.label(core)
    if n>1:
        sz=ndi.sum(core,lab,range(1,n+1)); core=lab==(1+int(np.argmax(sz)))
    return core
def feats(name,pre,fr,f):
    core=body(fr); L=oklab_L(fr[...,:3].astype(float)); a=fr[...,3]
    ys,xs=np.nonzero(core)
    if len(ys)<30: return None
    bl=xs.max()-xs.min()+1; bh=ys.max()-ys.min()+1
    NB=5; acc=np.zeros(NB); cnt=np.zeros(NB)
    rev=[];cols=0
    for x in range(xs.min(),xs.max()+1):
        c=np.nonzero(core[:,x])[0]
        if len(c)<6: continue
        t=(c-c.min())/(c.max()-c.min()); b=np.minimum((t*NB).astype(int),NB-1)
        for i in range(NB):
            sel=b==i
            if sel.any(): acc[i]+=L[c[sel],x].mean(); cnt[i]+=1
        v=L[c,x]; d=np.sign(np.diff(v)*(np.abs(np.diff(v))>0.04))
        d=d[d!=0]; rev.append(int((np.diff(d)!=0).sum()) if len(d)>1 else 0); cols+=1
    prof=acc/np.maximum(cnt,1)
    op=a>=200; cols_rgb=fr[op][:,:3]
    ncol=len(np.unique(cols_rgb,axis=0))
    inter=ndi.binary_erosion(core,iterations=1)
    # texture: local contrast between 4-neighbours inside body
    dx=np.abs(np.diff(L,axis=1)); dy=np.abs(np.diff(L,axis=0))
    mx=(inter[:,1:]&inter[:,:-1]); my=(inter[1:]&inter[:-1])
    tex=np.concatenate([(dx[mx]>0.05),(dy[my]>0.05)]).mean() if mx.sum() else 0
    # checker/isolated pixels: neighbours both sides equal colour and differ from centre
    P=fr[...,:3].astype(int)
    def eq(a,b): return (a==b).all(-1)
    c=P[1:-1,1:-1]
    chk=(eq(P[1:-1,:-2],P[1:-1,2:])&~eq(c,P[1:-1,:-2])&eq(P[:-2,1:-1],P[2:,1:-1])&~eq(c,P[:-2,1:-1]))&inter[1:-1,1:-1]
    iso=chk.sum()/max(inter.sum(),1)
    # highlight: top 12% L inside body -> compactness (fill of its bbox) and bbox aspect
    Lb=L[core]; th=np.percentile(Lb,88); hm=core&(L>=th)
    hy,hx=np.nonzero(hm)
    hl_w=(hx.max()-hx.min()+1)/bl; hl_h=(hy.max()-hy.min()+1)/bh
    fill=hm.sum()/((hx.max()-hx.min()+1)*(hy.max()-hy.min()+1))
    # light centroid vertical position (0 top,1 bottom) inside body bbox
    hcy=(hy.mean()-ys.min())/bh
    return dict(name=name,pre=pre,bl=int(bl),bh=int(bh),asp=round(bl/bh,2),area=int(core.sum()),
        prof=[round(float(v),3) for v in prof],lowdelta=round(float(prof[-2:].mean()-prof[:2].mean()),3),
        Lrange=round(float(np.percentile(Lb,95)-np.percentile(Lb,5)),3),Lstd=round(float(Lb.std()),3),
        ncol=int(ncol),tex=round(float(tex),3),chk=round(float(iso),4),rev=round(float(np.mean(rev)),2) if rev else 0,
        hl_w=round(float(hl_w),2),hl_h=round(float(hl_h),2),hl_fill=round(float(fill),2),hcy=round(float(hcy),2),f=f)
if __name__=='__main__':
    res={}
    for p in BI:
        res[p]=[r for r in (feats(*x) for x in load(p)) if r]
    json.dump(res,open(os.path.join(v4env.CACHE,'feats.json'),'w'))
    for p,v in res.items():
        g=lambda k:np.median([r[k] for r in v])
        print(p,len(v),'asp',g('asp'),'area',g('area'),'lowdelta',g('lowdelta'),'Lrange',g('Lrange'),'Lstd',g('Lstd'),'ncol',g('ncol'),'tex',g('tex'),'chk',g('chk'),'rev',g('rev'),'hcy',g('hcy'),'hlfill',g('hl_fill'))
