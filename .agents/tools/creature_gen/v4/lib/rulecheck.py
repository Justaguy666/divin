import v4env  # noqa: F401  (paths)
"""Pass/fail of a pilot sprite against the reference bands from the sprite-grammar study."""
import os,sys,glob,re,numpy as np

from f2 import feat,lab
import f3 as _f3
from m import body
from huecl import hue_cluster
from lp255 import lp255
from plateau import plateau
from hlmet import hlmet
from PIL import Image
src=open(os.path.join(v4env.GEN,'study','jag.py')).read().split('for pre in')[0]
src=src.replace("STUDY = _os.path.dirname(_os.path.abspath(__file__))","STUDY=%r"%os.path.join(v4env.GEN,'study'))
_g={}; exec(src,_g); jag=_g['jag']
WATER=v4env.WATER
def ad(x,y): return abs((x-y+180)%360-180)
def measure(f,pre):
    mm=re.search(r'_swim_(\d+)x(\d+)_4f',f); W,H=int(mm[1]),int(mm[2]); full=np.array(Image.open(f).convert('RGBA')); fr=full[:H,:W]
    r=feat(fr); q=_f3.feat3(fr); hc=hue_cluster(fr); core=body(fr); L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b)
    ys,xs=np.nonzero(core); x0,x1=xs.min(),xs.max(); bot=[];abv=[]
    for x in range(x0+int((x1-x0)*.3),x0+int((x1-x0)*.7)):
        c=np.nonzero(core[:,x])[0]
        if c[-1]+1<fr.shape[0] and fr[c[-1]+1,x,3]>0: continue   # a fin is attached below: no belly outline in this column
        bot.append(L[c[-1],x]); abv.append(L[c[-2],x])
    if not bot: bot,abv=[np.nan],[np.nan]
    runs=[]
    for x in range(x0+int((x1-x0)*.3),x0+int((x1-x0)*.7)):
        c=np.nonzero(core[:,x])[0]; k=0
        for val in L[c[::-1],x]:
            if val<0.26: k+=1
            else: break
        runs.append(k)
    from scipy import ndimage as _ndi
    from finsplit import fin_split
    fin_clear,fin_vivid=fin_split(fr,core,L,C,a,b)
    _lp=lp255(fr)[1]; len_amp=float(np.nanmax(_lp[1:9])-_lp[0])
    lp=np.array(r['lenprof'],float); A=fr[...,3]; fin=(A>0)&(A<255); al=A[fin].astype(float)
    # muted body colours only; saturated accents (fins, spots) are allowed complements
    m=core&(C>=0.025)&(C<0.09); hh=np.degrees(np.arctan2(b[m],a[m])); d=np.abs((hh-WATER[pre][0]+180)%360-180)
    ac=all((full[k*H:(k+1)*H,0:W]==full[k*H:(k+1)*H,2*W:3*W]).all() for k in range(6))
    return dict(lightzone=q['lightzone'],cshade=q['cshade'],darkthick=float((L[core]<0.35).mean()) if core.sum() else 0.0,outl=float(np.median(runs)),bottom=float(np.median(bot)),above=float(np.median(abv)),
        eyedom=q['eyedom'],pupil=q['pupil'],floor_gap=r['Lp5']-q['pupil'],lp_peak=lp255(fr)[0],head_lt_peak=float(lp255(fr)[1][9]<np.nanmax(lp255(fr)[1][1:-1])),
        fam_hue=hc['fam_hue'] if hc else np.nan,cmid=hc['cmid'] if hc else np.nan,hue_lt=hc['hue_lt'] if hc else np.nan,hue_dk=hc['hue_dk'] if hc else np.nan,clt=hc['clt'] if hc else np.nan,cdk=hc['cdk'] if hc else np.nan,
        marks=r['mark_n'],singletons=r['singletons'],fin_alpha=float(np.median(al)) if len(al) else np.nan,fin_spread=float(np.percentile(al,90)-np.percentile(al,10)) if len(al) else np.nan,
        hl_cover=hlmet(core,L)[0],hl_spread=hlmet(core,L)[1],hl_topgap=hlmet(core,L)[2],body_mean=float(L[core].mean()),body_c=float(np.median(C[core])),plateau=plateau(fr,core,L)[0],body_bg_cs=float(L[core].mean()-WATER[pre][1]),fin_dL=r['fin_dL'],fin_clear=fin_clear,fin_vivid=fin_vivid,len_amp=len_amp,fin_share=r['fin_share'],jag=jag(f),discord=float(((d>45)&(d<110)).mean()) if m.sum()>=30 else 0.0,body_bg=float(L[core].mean()-WATER[pre][1]),AC=float(ac))
BANDS=dict(ident_dL=(-0.10,0.10),ident_C=(0.8,1.6),body_bg_cs=(-1,-0.06),cshade=(-0.24,0.05),darkthick=(0.10,0.30),outl=(0,1),bottom=(0.19,0.35),above=(0.32,1),eyedom=(0,0.01),pupil=(0.13,0.17),floor_gap=(0.04,1),
    hue_lt=(2,15),hue_dk=(0,12),clt=(0.80,1.10),cdk=(0.50,0.76),marks=(6,11),singletons=(0.42,0.54),fin_alpha=(165,210),fin_spread=(30,58),
    fin_clear=(0.10,0.18),fin_vivid=(0.04,0.20),len_amp=(0.10,0.22),jag=(0,0.10),discord=(0,0.05),AC=(1,1))
SMALL=dict(fin_clear=(0.10,0.27),hue_lt=None,hue_dk=None,clt=None,cdk=None,lightzone=(0.25,0.65),cshade=(-0.30,0.0),darkthick=(0.08,0.34),above=(0.30,1),marks=(3,10),fin_dL=(0.15,0.27),discord=None)
def check(f,pre,small=False,base_disc=0.0,base_file=None):
    v=measure(f,pre); out={}
    if base_file:   # species identity: the body keeps roughly its installed lightness and colourfulness
        b=measure(base_file,pre); v['ident_dL']=v['body_mean']-b['body_mean']; v['ident_C']=v['body_c']/max(b['body_c'],1e-3)
    else: v['ident_dL']=0.0; v['ident_C']=1.0
    for k,bnd in BANDS.items():
        if small and k in SMALL: bnd=SMALL[k]
        if bnd is None: out[k]=(v[k],None,None); continue
        if isinstance(v[k],float) and np.isnan(v[k]): out[k]=(v[k],None,None); continue   # no such fins on this species
        if k=='hue_lt' and abs(((v['fam_hue']-100+180)%360)-180)<=15: bnd=(-3,15)   # a yellow family cannot turn further toward yellow
        if k in ('clt','cdk') and v['cmid']<0.035: out[k]=(v[k],None,None); continue   # near-neutral silver: chroma ratios are noise
        if k=='discord': bnd=(0,max(bnd[1],base_disc+0.01))   # never stricter than the approved sheet
        out[k]=(v[k],bnd,bool(bnd[0]-1e-9<=v[k]<=bnd[1]+1e-9))
    out['body_bg']=(v['body_bg'],None,None); out['fin_share']=(v['fin_share'],None,None)
    return out
def report(rows):
    keys=list(rows[0][1].keys())
    for name,res in rows:
        fails=[f'{k}={res[k][0]:.2f} (cần {res[k][1][0]:g}–{res[k][1][1]:g})' for k in keys if res[k][2] is False]
        print(f'{name}: {"ĐẠT" if not fails else str(len(fails))+" lệch"}', '; '.join(fails))
