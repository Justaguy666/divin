import v4env  # noqa: F401  (paths)
"""fincheck2 + motion signature per fin kind (AC/BW/PF): dorsal and ventral move at the tips, modestly, not as a mirror of the tail."""
import sys,numpy as np
import fincheck2 as F2
from phase import sig
F2.B[('caudal','m_change')]=(0.60,1)
MB={('dorsal','mag'):(0.18,0.42),('ventral','mag'):(0.25,0.66),('dorsal','base_change'):(0,0.36),('ventral','base_change'):(0,0.45)}
SCALE=dict(F2.SCALE); SCALE.update(mag=0.05,base_change=0.05)
B=F2.B
def edge_touch(f): return F2.edge_touch(f)
def measure(f,base_file=None):
    st=F2.measure(f,base_file); sg=sig(f)
    for g,v in sg.items():
        if g in st: st[g]['mag']=v['mag']; st[g]['base_change']=v['base_change']
    return st
def check(st):
    out=F2.check(st)
    for (g,k),b in MB.items():
        x=st.get(g,{}).get(k,np.nan); out[f'fin_{g}_{k}']=(x,b,None) if x!=x else (float(x),b,bool(b[0]<=x<=b[1]))
    return out
