import v4env  # noqa: F401  (paths)
import sys,glob,re,numpy as np

from scipy import ndimage as ndi
from m import body
from f2 import lab
from PIL import Image
def pe(f):
    W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',f).groups()); fr=np.array(Image.open(f).convert('RGBA'))[:H,:W]; core=body(fr); L=lab(fr[...,:3].astype(float))[0]
    t=np.percentile(L[core],98)-0.06; w=core&(L>=t); lb,k=ndi.label(w)
    if not k: return [0,0,0,0]
    s=ndi.sum(w,lb,range(1,k+1)); P=lb==(int(np.argmax(s))+1); ring=ndi.binary_dilation(P)&~P&core
    ys,xs=np.nonzero(P); cx=np.nonzero(core)[1]
    return [s.max()/core.sum(),(xs.max()-xs.min()+1)/(cx.max()-cx.min()+1),float(np.median(L[P])-np.median(L[ring])) if ring.sum() else 0,(ys.max()-ys.min()+1)]
