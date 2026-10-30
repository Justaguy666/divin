import v4env  # noqa: F401  (paths)
import re,numpy as np
from PIL import Image
from scipy import ndimage as ndi
import sys
from m import body
from f2 import lab
def fr0(p):
    W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',p).groups()); return np.array(Image.open(p).convert('RGBA'))[:H,:W]
def nat(fr,bg):
    a=fr[...,3:]/255.; return (fr[...,:3]*a+np.array(bg)*(1-a)).astype(np.uint8)
def diag(fr):
    core=body(fr); L=lab(fr[...,:3].astype(float))[0]; A=fr[...,3]; img=np.full(fr.shape[:2]+(3,),30,np.uint8)
    g=(np.clip(L,0,1)*200).astype(np.uint8); img[A>0]=np.stack([g,g,g],-1)[A>0]
    Lc=L[core]; img[core&(L>=np.percentile(Lc,90))]=(255,210,0)
    key=(fr[...,0].astype(np.int64)<<16)|(fr[...,1].astype(np.int64)<<8)|fr[...,2]; best=None
    for k in np.unique(key[core]):
        lb,n=ndi.label(core&(key==k))
        for i in range(1,n+1):
            s=(lb==i).sum()
            if best is None or s>best[0]: best=(s,lb==i)
    img[best[1]]=(img[best[1]]*0.4+np.array([200,40,40])*0.6).astype(np.uint8)
    P=fr[...,:3].astype(int); eq=lambda u,v:(u==v).all(-1); inr=ndi.binary_erosion(core); c=P[1:-1,1:-1]; nb=[P[:-2,1:-1],P[2:,1:-1],P[1:-1,:-2],P[1:-1,2:]]
    iso=np.zeros_like(core); iso[1:-1,1:-1]=inr[1:-1,1:-1]&eq(nb[0],nb[1])&eq(nb[1],nb[2])&eq(nb[2],nb[3])&~eq(c,nb[0]); img[iso]=(255,0,255)
    finj=core&ndi.binary_dilation((A>0)&(A<250))&~ndi.binary_dilation(A==0); img[finj]=(0,200,255)
    return img, dict(largest=best[0]/core.sum(), isolated=int(iso.sum()))
