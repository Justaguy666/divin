import v4env  # noqa: F401  (paths)
"""v4 checks = v3 + BW-style light handling: the brightest 10% only one small step above its surroundings, light in the upper third, back not darker than the body."""
import sys,numpy as np
import rulecheck3 as R3
from hlstudy import hl
import os
HL=dict(hl_step_ring=(0.06,0.18),hl_major_step=(0.06,0.13),hl_top_t=(0.26,float(os.environ.get('R4_TOPT_MAX','0.42'))),hl_back=(-0.02,0.16))
R3.SCALE.update(hl_step_ring=0.03,hl_major_step=0.02,hl_top_t=0.03,hl_back=0.03)
SCALE=R3.SCALE
def measure(f,base_file,pre='cs'):
    v=R3.measure(f,base_file,pre); h=hl(f)
    v.update(hl_step_ring=h['step_ring'],hl_major_step=h['major_top_step'],hl_top_t=h['top_t'],hl_back=h['back']); return v
def check(v,small):
    out=R3.check(v,small)
    for k,b in HL.items():
        x=v.get(k,np.nan); out[k]=(x,b,None) if x!=x else (float(x),b,bool(b[0]<=x<=b[1]))
    return out
