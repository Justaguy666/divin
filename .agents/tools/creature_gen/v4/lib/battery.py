import v4env  # noqa: F401  (paths)
"""Broad, rule-independent feature battery for swimmer sprites (row 0 = facing east). ~90 features."""
import os,re,glob,json,sys,math
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

from m import body
from f2 import lab
WATER=v4env.WATER
def circstd(h,w):
    z=(w*np.exp(1j*np.radians(h))).sum()/max(w.sum(),1e-9); return float(np.degrees(np.sqrt(-2*np.log(max(abs(z),1e-9)))))
def ccomp(mask,P):
    """same-colour 4-connected components inside mask"""
    key=(P[...,0].astype(np.int64)<<16)|(P[...,1].astype(np.int64)<<8)|P[...,2]; sizes=[]
    for k in np.unique(key[mask]):
        lb,n=ndi.label(mask&(key==k)); 
        if n: sizes+=list(ndi.sum(np.ones_like(lb),lb,range(1,n+1)))
    return np.array(sizes)
def runs(mask,P,axis):
    key=(P[...,0].astype(np.int64)<<16)|(P[...,1].astype(np.int64)<<8)|P[...,2]; key=np.where(mask,key,-1)
    if axis==0: key=key.T
    out=[]
    for row in key:
        r=0;prev=None
        for v in row:
            if v>=0 and v==prev: r+=1
            else:
                if prev is not None and prev>=0: out.append(r)
                r=1 if v>=0 else 0
            prev=v
        if prev is not None and prev>=0: out.append(r)
    return np.array(out) if out else np.array([0])
def feats(path,pre):
    im=np.array(Image.open(path).convert('RGBA')); W,H=map(int,re.search(r'_(\d+)x(\d+)_4f',path).groups())
    nr=im.shape[0]//H; FR=[[im[r*H:(r+1)*H,k*W:(k+1)*W] for k in range(4)] for r in range(nr)]
    fr=FR[0][0]; A=fr[...,3]; vis=A>0; op=A>=250; core=body(fr)
    L,a,b=lab(fr[...,:3].astype(float)); C=np.hypot(a,b); h=np.degrees(np.arctan2(b,a)); P=fr[...,:3]
    ys,xs=np.nonzero(core); x0,x1,y0,y1=xs.min(),xs.max(),ys.min(),ys.max(); BL=x1-x0+1; BH=y1-y0+1
    U=(np.arange(W)[None,:]-x0)/max(BL-1,1)+0*L; T=np.zeros_like(L)
    for x in range(x0,x1+1):
        c=np.nonzero(core[:,x])[0]
        if len(c): T[:,x]=(np.arange(H)-c.min())/max(c.max()-c.min(),1)
    o={}
    # ---- geometry
    o['g_BL']=BL; o['g_aspect']=BL/BH; o['g_canvas_fillx']=BL/W; o['g_canvas_filly']=BH/H
    vy,vx=np.nonzero(vis); o['g_vis_over_core']=vis.sum()/core.sum(); o['g_opaque_fin_share']=(op&~core).sum()/core.sum()
    o['g_translucent_share']=(vis&~op).sum()/core.sum(); o['g_tail_len']=(x0-vx.min())/BL; o['g_fin_above']=(y0-vy.min())/BH; o['g_fin_below']=(vy.max()-y1)/BH
    per=(vis&~ndi.binary_erosion(vis)).sum(); o['g_compact']=per**2/vis.sum()
    cper=(core&~ndi.binary_erosion(core)).sum(); o['g_core_compact']=cper**2/core.sum()
    # silhouette smoothness of the core outline: run lengths of the top edge (stair steps)
    top=np.array([np.nonzero(core[:,x])[0].min() for x in range(x0,x1+1)]); bot=np.array([np.nonzero(core[:,x])[0].max() for x in range(x0,x1+1)])
    dt=np.diff(top); o['g_top_jumps']=float((np.abs(dt)>1).mean()); o['g_top_reversals']=float((np.diff(np.sign(dt[dt!=0]))!=0).sum()/BL) if (dt!=0).sum()>1 else 0.0
    o['g_maxdepth_u']=float(np.argmax(bot-top)/BL)
    # ---- palette
    Pv=P[vis]; o['p_ncol_vis']=len(np.unique(Pv,axis=0)); Pc=P[core]; cols,cnt=np.unique(Pc,axis=0,return_counts=True)
    o['p_ncol_core']=len(cols); o['p_ncol_per100']=len(cols)/core.sum()*100; o['p_top3']=np.sort(cnt)[::-1][:3].sum()/cnt.sum(); o['p_once']=(cnt==1).mean()
    cL=lab(cols.astype(float))[0]; lv=[]
    for i in np.argsort(cL):
        if lv and cL[i]-lv[-1]<0.02: continue
        lv.append(cL[i])
    st=np.diff(lv) if len(lv)>1 else np.array([0.0]); o['p_levels']=len(lv); o['p_step_med']=float(np.median(st)); o['p_step_max']=float(st.max())
    Lc=L[core]; Cc=C[core]; hc=h[core]
    o['t_L05']=np.percentile(Lc,5); o['t_L50']=np.percentile(Lc,50); o['t_L95']=np.percentile(Lc,95); o['t_Lrange']=o['t_L95']-o['t_L05']; o['t_Lstd']=Lc.std()
    o['c_C50']=np.median(Cc); o['c_C90']=np.percentile(Cc,90); o['c_Cmax']=Cc.max(); o['c_Cstd']=Cc.std()
    ch=Cc>=0.03; o['c_chromatic_share']=ch.mean()
    o['c_hue_spread']=circstd(hc[ch],Cc[ch]) if ch.sum()>5 else 0.0
    hist=np.zeros(12)
    for hh,cc in zip(hc[ch],Cc[ch]): hist[int(((hh%360)//30))]+=1
    o['c_hue_families']=int((hist/max(hist.sum(),1)>=0.08).sum())
    o['c_LC_corr']=float(np.corrcoef(Lc,Cc)[0,1]) if Cc.std()>1e-4 else 0.0
    o['t_Lmin_vis']=float(L[vis&(A>=250)].min()); o['t_Lmax_vis']=float(L[vis&(A>=250)].max())
    o['w_dL']=float(Lc.mean()-WATER[pre][1])
    # ---- shading structure
    inr=ndi.binary_erosion(core)
    tt=T[core]; o['s_vslope']=float(np.polyfit(tt,Lc,1)[0]); q=np.polyfit(tt,Lc,2); o['s_vcurv']=float(q[0])
    uu=U[core]; o['s_hslope']=float(np.polyfit(uu,Lc,1)[0]); o['s_hcurv']=float(np.polyfit(uu,Lc,2)[0])
    edt=ndi.distance_transform_edt(core); o['s_edge_corr']=float(np.corrcoef(edt[core],Lc)[0,1])
    gy,gx=np.gradient(np.where(core,L,np.nan)); ey,ex=np.gradient(edt.astype(float)); g=np.hypot(gx,gy); m=inr&(np.nan_to_num(g)>0.02)
    if m.sum()>3:
        cosE=(gx*ex+gy*ey)[m]/(g[m]*np.maximum(np.hypot(ex,ey)[m],1e-6)); o['s_grad_edge']=float(np.nanmean(cosE)); o['s_grad_up']=float(np.nanmean(-gy[m]/g[m])); o['s_grad_fwd']=float(np.nanmean(gx[m]/g[m]))
    else: o['s_grad_edge']=o['s_grad_up']=o['s_grad_fwd']=0.0
    hi=core&(L>=np.percentile(Lc,80)); hy,hx=np.nonzero(hi); o['s_light_u']=float(U[hi].mean()); o['s_light_t']=float(T[hi].mean())
    lo_=core&(L<=np.percentile(Lc,20)); o['s_dark_u']=float(U[lo_].mean()); o['s_dark_t']=float(T[lo_].mean())
    head=core&(U>0.8); mid=core&(U>0.35)&(U<0.65); tail=core&(U<0.2); o['s_head_minus_mid']=float(L[head].mean()-L[mid].mean()); o['s_tail_minus_mid']=float(L[tail].mean()-L[mid].mean()) if tail.sum() else 0.0
    # ---- pixel clusters / texture
    sz=ccomp(core,P); o['x_comp_mean']=float(sz.mean()); o['x_comp_per100']=len(sz)/core.sum()*100; o['x_comp_single']=float((sz==1).mean()); o['x_comp_largest']=float(sz.max()/core.sum())
    o['x_run_h']=float(runs(core,P,1).mean()); o['x_run_v']=float(runs(core,P,0).mean())
    dxL=np.abs(np.diff(L,axis=1)); dyL=np.abs(np.diff(L,axis=0)); mx=inr[:,1:]&inr[:,:-1]; my=inr[1:]&inr[:-1]; d=np.concatenate([dxL[mx],dyL[my]])
    o['x_edge_density']=float((d>0.005).mean()); o['x_lc_mean']=float(d.mean()); o['x_lc_p90']=float(np.percentile(d,90)); o['x_hard_edges']=float((d>0.10).mean())
    dC=np.concatenate([np.abs(np.diff(C,axis=1))[mx],np.abs(np.diff(C,axis=0))[my]]); o['x_chroma_lc']=float(dC.mean())
    Pi=P.astype(int); eq=lambda u,v:(u==v).all(-1); c_=Pi[1:-1,1:-1]
    nb=[Pi[:-2,1:-1],Pi[2:,1:-1],Pi[1:-1,:-2],Pi[1:-1,2:]]
    iso=inr[1:-1,1:-1]&eq(nb[0],nb[1])&eq(nb[1],nb[2])&eq(nb[2],nb[3])&~eq(c_,nb[0]); o['x_isolated']=float(iso.sum()/inr.sum())
    chk=inr[1:-1,1:-1]&eq(nb[2],nb[3])&~eq(c_,nb[2])&eq(nb[0],nb[1])&~eq(c_,nb[0])&~eq(nb[0],nb[2]); o['x_dither']=float(chk.sum()/inr.sum())
    med=ndi.median_filter(np.where(core,L,np.nan),size=5,mode='nearest'); dev=np.where(core,np.abs(L-np.nan_to_num(med)),0)
    mk=core&(dev>0.08); lb,n=ndi.label(mk); o['x_marks']=n; o['x_mark_cover']=float(mk.sum()/core.sum())
    if n:
        el=[]
        for s_ in ndi.find_objects(lb): el.append((s_[1].stop-s_[1].start)/(s_[0].stop-s_[0].start))
        o['x_mark_horiz']=float(np.median(el))
    else: o['x_mark_horiz']=1.0
    # ---- outline by side (core pixels touching full transparency)
    def side(dy_,dx_):
        vals=[];cr=[];hs=[]
        for j,i in zip(*np.nonzero(core)):
            jj,ii=j+dy_,i+dx_
            if 0<=jj<H and 0<=ii<W and A[jj,ii]==0:
                ji,ii2=j-2*dy_,i-2*dx_
                if 0<=ji<H and 0<=ii2<W and core[ji,ii2]:
                    vals.append(L[j,i]-L[ji,ii2]); cr.append(C[j,i]/max(C[ji,ii2],0.01))
        return (float(np.median(vals)) if vals else np.nan, float(np.median(cr)) if cr else np.nan, len(vals))
    for nm,(dy_,dx_) in dict(top=(-1,0),bot=(1,0),front=(0,1),back=(0,-1)).items():
        v,c2,n2=side(dy_,dx_); o[f'o_{nm}_dL']=v; o[f'o_{nm}_Cratio']=c2
    edgepx=core&~ndi.binary_erosion(core); o['o_edge_L']=float(L[edgepx].mean()); o['o_edge_minus_core']=float(L[edgepx].mean()-L[inr].mean())
    finj=core&ndi.binary_dilation(vis&~op)&~ndi.binary_dilation(~vis); o['o_finjunction_dL']=float(L[finj].mean()-L[inr].mean()) if finj.sum() else np.nan
    # ---- eye: darkest small cluster in the front third of the core interior
    fz=inr&(U>0.6)
    if fz.sum():
        Lf=np.where(fz,L,9); j,i=np.unravel_index(np.argmin(Lf),L.shape); pl=L[j,i]; pm=fz&(L<=pl+0.03); lb,_=ndi.label(pm); pup=lb==lb[j,i]
        ring=ndi.binary_dilation(pup,iterations=1)&~pup&core
        o['e_pupil_L']=float(pl); o['e_pupil_px']=int(pup.sum()); o['e_ring_L']=float(L[ring].mean()) if ring.sum() else np.nan; o['e_ring_maxL']=float(L[ring].max()) if ring.sum() else np.nan
        o['e_contrast']=o['e_ring_maxL']-pl; o['e_ring_C']=float(C[ring].max()) if ring.sum() else np.nan
        o['e_u']=float(U[j,i]); o['e_t']=float(T[j,i]); o['e_catchlight']=float(ring.sum() and L[ring].max()>np.percentile(Lc,90))
        o['e_size_rel']=float((pup|ring).sum()/BH)
    # ---- fins
    fin=vis&~core; fa=A[fin].astype(float)
    if fin.sum()>=4:
        o['f_alpha_med']=float(np.median(fa)); o['f_alpha_p10']=float(np.percentile(fa,10)); o['f_alpha_p90']=float(np.percentile(fa,90)); o['f_opaque_share']=float((fa>=250).mean())
        o['f_L_minus_body']=float(np.median(L[fin])-np.median(Lc)); o['f_C_ratio']=float(np.median(C[fin])/max(np.median(Cc),0.01))
        fh=h[fin&(C>=0.03)]; bh_=np.degrees(np.angle(np.exp(1j*np.radians(hc[ch])).mean())) if ch.sum() else 0
        o['f_hue_diff']=float(np.abs((np.median(fh)-bh_+180)%360-180)) if len(fh)>3 else 0.0
        o['f_ncol']=len(np.unique(P[fin],axis=0)); fe=fin&~ndi.binary_erosion(fin); fi=fin&ndi.binary_erosion(fin)
        o['f_rim_dL']=float(L[fe].mean()-L[fi].mean()) if fi.sum() else np.nan; o['f_rim_dA']=float(A[fe].mean()-A[fi].mean()) if fi.sum() else np.nan
        fl=np.concatenate([np.abs(np.diff(L,axis=1))[(fin[:,1:]&fin[:,:-1])],np.abs(np.diff(L,axis=0))[(fin[1:]&fin[:-1])]]); o['f_texture']=float(fl.mean()) if len(fl) else 0.0
        o['f_alpha_levels']=len(np.unique(fa))
    # ---- animation (row 0, 4 frames)
    ch_=[];chc=[];chf=[];newc=[]; base=set(map(tuple,P[vis]))
    for k in range(1,4):
        f2=FR[0][k]; d_=(np.abs(f2.astype(int)-FR[0][k-1].astype(int)).sum(-1)>0)&((f2[...,3]>0)|(FR[0][k-1][...,3]>0))
        ch_.append(d_.sum()/vis.sum()); newc.append(len(set(map(tuple,f2[...,:3][f2[...,3]>0]))-base))
        cb=body(f2); chc.append(((np.abs(f2.astype(int)-FR[0][k-1].astype(int)).sum(-1)>0)&cb).sum()/cb.sum())
    o['a_change']=float(np.mean(ch_)); o['a_core_change']=float(np.mean(chc)); o['a_new_colours']=float(np.mean(newc))
    o['a_A_eq_C']=float((FR[0][0]==FR[0][2]).all())
    cy=[np.nonzero(body(FR[0][k]))[0].mean() for k in range(4)]; o['a_bob']=float(np.ptp(cy))
    tx=[np.nonzero(FR[0][k][...,3]>0)[1].min() for k in range(4)]; o['a_tail_sweep']=float(np.ptp(tx))
    allc=set(map(tuple,im[...,:3][im[...,3]>0])); o['a_sheet_ncol']=len(allc); o['a_sheet_vs_frame']=len(allc)/max(o['p_ncol_vis'],1)
    return {k:(float(v) if v is not None else np.nan) for k,v in o.items()}
