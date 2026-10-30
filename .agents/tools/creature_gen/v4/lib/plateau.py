import v4env  # noqa: F401  (paths)
import numpy as np
from scipy import ndimage as ndi
def plateau(fr,core,L):
    """largest connected patch of the sprite's own top values (within 0.06 of its 98th percentile), as a share of the body"""
    t=np.percentile(L[core],98)-0.06; w=core&(L>=t); lb,k=ndi.label(w)
    return float((max(ndi.sum(w,lb,range(1,k+1))) if k else 0)/core.sum()), float(w.sum()/core.sum())
