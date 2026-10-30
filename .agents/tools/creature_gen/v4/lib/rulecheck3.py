import v4env  # noqa: F401  (paths)
"""Acceptance checks v3: reference p10-p90 bands from the broad battery + the still-valid v2 checks.
Bands are taken from the 89 AC/BW/PF swimmers (neutral/colour strata where colour behaves differently)."""
import sys,os,glob,json,re,numpy as np
import rulecheck as C2
from battery import feats
from platedge import pe
OLD=dict(ident_dL=(-0.10,0.10),ident_C=(0.8,1.6),body_bg_cs=(-1,-0.06),cshade=(-0.28,0.11),darkthick=(0.07,0.46),outl=(0,1),bottom=(0.17,0.40),above=(0.25,0.72),
         eyedom=(0,0.01),hue_lt=(-1.9,14.8),hue_dk=(-2.7,15.9),marks=(3,15),len_amp=(0.08,0.22),jag=(0,0.10),discord=(0,0.05),AC=(1,1),fin_clear=(0.05,0.24),fin_vivid=(0.04,0.20))
CHROMA={'neutral':dict(clt=(0.54,1.25),cdk=(0.60,1.03),plat_share=(0,0.17),plat_h=(0,5)),'colour':dict(clt=(0.74,1.16),cdk=(0.38,0.90),plat_share=(0,0.29),plat_h=(0,7))}
NEW=dict(p_top3=(0.0,0.59),x_comp_largest=(0.0,0.26),t_L95=(0.72,0.91),t_Lrange=(0.47,0.70),x_isolated=(0,0.014),x_comp_single=(0.43,0.68),
         o_finjunction_dL=(-0.33,-0.13),f_alpha_levels=(19,43),f_alpha_p10=(130,202),f_alpha_med=(155,216),f_texture=(0.049,0.113),e_contrast=(0.68,0.81),
         e_pupil_L=(0.144,0.172),s_tail_minus_mid=(-0.135,-0.03),o_top_Cratio=(0.67,1.6),s_vslope=(-0.315,0.047),s_light_t=(0.32,0.59),
         plat_share=(0.0,0.17),plat_h=(0,5))
SMALL=dict(fin_clear=(0.05,0.27),marks=(1,10),hue_lt=None,hue_dk=None,clt=None,cdk=None,cshade=(-0.30,0.11),above=(0.25,1),x_comp_single=(0.3,0.75),f_alpha_levels=(10,43),f_texture=(0.03,0.113))
SCALE=dict(ident_dL=0.03,ident_C=0.1,body_bg_cs=0.03,cshade=0.04,darkthick=0.04,outl=0.5,bottom=0.03,above=0.04,eyedom=0.01,hue_lt=2,hue_dk=2,clt=0.08,cdk=0.08,marks=2,len_amp=0.03,
           jag=0.03,discord=0.02,fin_clear=0.03,fin_vivid=0.03,p_top3=0.04,x_comp_largest=0.03,t_L95=0.03,t_Lrange=0.03,x_isolated=0.004,x_comp_single=0.04,o_finjunction_dL=0.04,
           f_alpha_levels=3,f_alpha_p10=10,f_alpha_med=10,f_texture=0.01,e_contrast=0.02,e_pupil_L=0.01,s_tail_minus_mid=0.02,o_top_Cratio=0.08,s_vslope=0.04,s_light_t=0.04,plat_share=0.03,plat_h=1)
def measure(f,base_file,pre='cs'):
    v=C2.measure(f,pre); b=feats(f,pre); p=pe(f); v.update({k:b.get(k,np.nan) for k in NEW if k in b}); v['plat_share']=p[0]; v['plat_h']=p[3]
    ref=C2.measure(base_file,pre); v['ident_dL']=v['body_mean']-ref['body_mean']; v['ident_C']=v['body_c']/max(ref['body_c'],1e-3); v['_base_disc']=ref['discord']; v['_pre']=pre
    return v
def check(v,small):
    out={}; bands=dict(OLD); bands.update(NEW); bands.update(CHROMA['neutral' if (v.get('cmid') is None or not v['cmid']>=0.04) else 'colour'])
    if small: bands.update(SMALL)
    bands['discord']=(0,max(0.05,v['_base_disc']+0.01))
    if not v4env.bright(v.get('_pre','cs')): bands['body_bg_cs']=(-0.05,1)   # dark water: the body sits a little above the water (v3 bracketing)
    for k,b in bands.items():
        x=v.get(k,np.nan)
        if b is None or x is None or (isinstance(x,float) and np.isnan(x)): out[k]=(x,b,None); continue
        out[k]=(float(x),b,bool(b[0]<=x<=b[1]))
    return out
