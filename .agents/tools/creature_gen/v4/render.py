"""Render one species with the v4 switches: python3 render.py <pre> <module> <name> <tag>; settings come from the environment
(PILOT_* globals and PILOT_<KEY>_<name> per species, see tune.py env_for / params/<pre>.json); writes
<PILOT_OUT>/<pre>_<name>_<tag>_<swim|crawl>_<W>x<H>_4f.png. Used by tune.py; build.py does the same into the install folder."""
import os,sys,importlib,math,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import v4env
pre,mod,name,tag=sys.argv[1:5]
os.environ['PRE']=pre
if os.environ.get('PILOT_STEER')=='1': os.environ['PILOT_WATER']=str(v4env.WATER[pre][0])
import swim,gait,pal
from PIL import Image
swim.use_v3(pre)
ROT=[float(x) for x in os.environ.get('PILOT_ROT_'+name, os.environ.get('PILOT_ROT','-5,-2.5,0,3,8,10')).split(',')]
CS=[float(x) for x in os.environ.get('PILOT_CS_'+name, os.environ.get('PILOT_CS','0.6,0.8,1,1,1,1')).split(',')]
WATER=v4env.WATER[pre][0] if pre in v4env.WATER else None
def warmshift(F):
    for k,tones in F.items():
        out=[]; cmid=float(np.mean([math.hypot(*pal.lab(t)[1:]) for t in tones[2:4]]))
        for i,h in enumerate(tones):
            L=pal.lab(h); a,b=L[1],L[2]; C=math.hypot(a,b)
            if C>=0.012:
                hd=math.degrees(math.atan2(b,a)); d=((100-hd+180)%360)-180; r=ROT[i]
                step=math.copysign(min(abs(r),abs(d)),d) if r>0 else -math.copysign(abs(r),d)
                if abs(d)<=15: step=0.0   # a yellow family stays put (it cannot turn further toward yellow, and away would read orange)
                if WATER is not None:
                    dn=abs(((hd+step)-WATER+180)%360-180); do=abs((hd-WATER+180)%360-180)
                    if 45<dn<110 and not (45<do<110): step=0.0   # never steer a tone into the discord band around the water hue
                    if 45<do<110 and os.environ.get('PILOT_STEER')=='1':   # a tone already in the band: move it out to the nearer edge (v3 steer rule)
                        sgn=1 if ((hd-WATER+180)%360-180)>0 else -1
                        step=(sgn*42.0+WATER-hd) if do<77.5 else (sgn*113.0+WATER-hd)
                        step=((step+180)%360)-180
                hn=math.radians(hd+step); C2=(cmid*CS[i]) if (os.environ.get('PILOT_CPROF')=='1' and cmid>=0.012 and i<2) else C*CS[i]; L=np.array([L[0],C2*math.cos(hn),C2*math.sin(hn)])
            out.append(pal.hexl(L))
        F[k]=out
if os.environ.get('PILOT_HUE')=='1': warmshift(pal.FAM)
if os.environ.get('PILOT_CRIMSON_'+name)=='1': pal.FAM['R1'][4]=pal.FAM['R1'][3]   # 'crimson-tinted' fins: the crimson tone, not its pale tint
m=importlib.import_module(mod)
def build(bodyL=None):
    F=getattr(m,name)(); g=gait.lookup(pre,name)
    if g and not getattr(F,'crawl',False): F.gait=g
    if os.environ.get('PILOT_LIGHTC','')!='keep' and hasattr(F,'lightc'): F.lightc=tuple(float(x) for x in os.environ.get('PILOT_LIGHTC_'+name, os.environ.get('PILOT_LIGHTC','0.40,0.45,1.0,1.6')).split(','))
    if 'PILOT_TSPANK_'+name in os.environ and hasattr(F,'tspan'): F.tspan*=float(os.environ['PILOT_TSPANK_'+name])
    if 'PILOT_TONE0' in os.environ and hasattr(F,'tone0'): F.tone0+=float(os.environ['PILOT_TONE0'])
    if 'PILOT_TONE0_'+name in os.environ and hasattr(F,'tone0'): F.tone0+=float(os.environ['PILOT_TONE0_'+name])
    if 'PILOT_TAILK_'+name in os.environ: os.environ['PILOT_TAILK']=os.environ['PILOT_TAILK_'+name]
    if 'PILOT_HEAD_'+name in os.environ: os.environ['PILOT_HEAD']=os.environ['PILOT_HEAD_'+name]
    if 'PILOT_RAMP0_'+name in os.environ: os.environ['PILOT_RAMP0']=os.environ['PILOT_RAMP0_'+name]
    if 'PILOT_SHOULDER_'+name in os.environ: swim.PILOT['shoulder']=float(os.environ['PILOT_SHOULDER_'+name])
    for _k in ('FINLOOP','LOOPK','FINBASEW','FINMOT','FINMOTL','RAYA','FAMID','FAK','FINGRAD','FINGS','RAYMIX','RIMDA','AMPV','AMPD','FINDL_CAUD','TOPSTEP','DITH','BANDW','BANDC','BANDU','MOT','MOTP','FINSTEP','RAYDL','FLOORREL','CATCH','FINJ'):
        if f'PILOT_{_k}_'+name in os.environ: os.environ['PILOT_'+_k]=os.environ[f'PILOT_{_k}_'+name]
    if 'PILOT_DKC_'+name in os.environ: os.environ['PILOT_DKC']=os.environ['PILOT_DKC_'+name]
    if 'PILOT_TMAX_'+name in os.environ: os.environ['PILOT_TMAX']=os.environ['PILOT_TMAX_'+name]
    if 'PILOT_CAP_'+name in os.environ: os.environ['PILOT_CAP']=os.environ['PILOT_CAP_'+name]
    if 'PILOT_FINK_'+name in os.environ: os.environ['PILOT_FINK']=os.environ['PILOT_FINK_'+name]
    if 'PILOT_PUPIL_'+name in os.environ: swim.PILOT['pupil']=os.environ['PILOT_PUPIL_'+name]
    if 'PILOT_VIVC_'+name in os.environ: os.environ['PILOT_VIVC']=os.environ['PILOT_VIVC_'+name]
    if 'PILOT_VIVL_'+name in os.environ: os.environ['PILOT_VIVL']=os.environ['PILOT_VIVL_'+name]
    if 'PILOT_OLC_'+name in os.environ: swim.PILOT['olc']=float(os.environ['PILOT_OLC_'+name])
    if 'PILOT_FINDL_'+name in os.environ: swim.PILOT['fin_dl']=float(os.environ['PILOT_FINDL_'+name])
    if 'PILOT_TEX_'+name in os.environ: swim.PILOT['tex']=float(os.environ['PILOT_TEX_'+name])
    F.pilot_bodyL=bodyL
    return F.sheet() if hasattr(F,'sheet') else swim.sheet(F)
sh,W,H,tags=build()
if swim.PILOT['fin']:
    from m import body as _body
    from f2 import lab as _lab
    fr=sh[:H,:W]; core=_body(fr); bl=float(_lab(fr[...,:3].astype(float))[0][core].mean())
    sh,W,H,tags=build(bl)
out=os.environ.get('PILOT_OUT',os.path.join(v4env.CACHE,'render')); os.makedirs(out,exist_ok=True)
kind='crawl' if (getattr(m,name)().__class__.__name__=='Crawler' or H*0+getattr(getattr(m,name)(),'crawl',False)) else 'swim'
Image.fromarray(sh,'RGBA').save(f'{out}/{pre}_{name}_{tag}_{kind}_{W}x{H}_4f.png'); print(pre,name,tag,W,H)
