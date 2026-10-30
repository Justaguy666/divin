"""drop specks of fewer than `n` pixels left detached from the animal (fin tips cut loose by tilt or ripple)."""
import numpy as np
from scipy import ndimage
def tidy(F, n=6):
    import swim
    base = F.sheet if hasattr(F, 'sheet') else (lambda F=F: swim.sheet(F))
    def sheet():
        sh, W, H, tags = base()
        for r in range(sh.shape[0] // H):
            for c in range(4):
                fr = sh[r * H:(r + 1) * H, c * W:(c + 1) * W]; lab, k = ndimage.label(fr[..., 3] > 0, structure=np.ones((3, 3)))
                for i in range(1, k + 1):
                    if (lab == i).sum() < n: fr[lab == i] = 0
        return sh, W, H, tags
    F.sheet = sheet; return F
