import v4env  # noqa: F401  (paths)
import numpy as np
from scipy import ndimage as ndi
def hlmet(core,L):
    t=np.percentile(L[core],85); w=core&(L>=t); ys,xs=np.nonzero(core); x0,x1=xs.min(),xs.max(); BL=x1-x0+1
    cols=[x for x in range(x0,x1+1) if w[:,x].any()]
    if not cols: return 0.0,9.0,9.0
    d=[np.nonzero(w[:,x])[0].min()-np.nonzero(core[:,x])[0].min() for x in cols]
    return len(cols)/BL, float(np.std(d)), float(np.median(d))
