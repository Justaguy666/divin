import v4env  # noqa: F401  (paths)
"""Fin checks v2: only rules that hold in all three reference dialects (AC, BW, PF), plus a canvas-edge guard for livelier fins."""
import sys,glob,re,numpy as np
from finstudy import study
from rimstudy import rim
from PIL import Image
B={('caudal','ray_aniso_A'):(0,0.70),('caudal','tex_A'):(0,9),('caudal','a_vs_dist'):(-1,-0.6),('caudal','ray_aniso_L'):(0.85,1.30),('caudal','inner_Lstd'):(0,0.08),
   ('caudal','ncol'):(8,40),('caudal','L_rel'):(0.0,0.25),('caudal','m_change'):(0.70,1),
   ('dorsal','ray_aniso_A'):(0,0.70),('dorsal','ray_aniso_L'):(0,1.15),('dorsal','ncol'):(8,40),('dorsal','L_rel'):(-0.06,0.16),('dorsal','tex_L'):(0.05,0.16),('dorsal','m_change'):(0.25,1),
   ('ventral','ray_aniso_A'):(0,0.70),('ventral','ray_aniso_L'):(0,1.15),('ventral','ncol'):(7,40),('ventral','L_rel'):(-0.03,0.18),('ventral','tex_L'):(0.05,0.18),('ventral','m_cy'):(0.18,2),('ventral','m_area'):(0.13,1)}
SCALE={'ray_aniso_A':0.08,'tex_A':1.5,'a_vs_dist':0.1,'ray_aniso_L':0.08,'inner_Lstd':0.01,'ncol':1.5,'L_rel':0.03,'m_change':0.06,'tex_L':0.01,'m_cy':0.05,'m_area':0.03,'edge':1}
def edge_touch(f):
    im=np.array(Image.open(f).convert('RGBA')); W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',f).groups()); n=0
    for r in range(im.shape[0]//H):
        for k in range(4):
            a=im[r*H:(r+1)*H,k*W:(k+1)*W,3]>0; n+=int(a[0].sum()+a[-1].sum()+a[:,0].sum()+a[:,-1].sum())
    return n
def measure(f,base_file=None):
    st=study(f); rm=rim(f)
    for g in rm:
        if g in st: st[g]['inner_Lstd']=rm[g]['inner_Lstd']
    st['edge']=edge_touch(f); st['edge_base']=edge_touch(base_file) if base_file else 0
    return st
def check(st):
    out={}
    for (g,k),b in B.items():
        x=st.get(g,{}).get(k,np.nan); out[f'fin_{g}_{k}']=(x,b,None) if x!=x else (float(x),b,bool(b[0]<=x<=b[1]))
    out['fin_edge']=(float(st['edge']),(0,st['edge_base']),bool(st['edge']<=st['edge_base']))
    return out
