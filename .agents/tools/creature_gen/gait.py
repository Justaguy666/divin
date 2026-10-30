"""Per-species swimming gait (v2 motion). Real fish move in different ways, and the ac / bw / pf references show it: a neon
only flicks the tail tip (8-10% of its pixels change), a cichlid ripples the soft dorsal and anal fins and rows with its
pectorals (25-35%, the tail only 40-60% of the motion), a gar or arowana sways the rear fins with the tail as one unit, a
knifefish moves only its ribbon fin, big slow fish beat at 5-6 fps and small darting ones at 10. A gait sets, per fin kind,
an amplitude multiplier on the fin's own flutter, how the dorsal / anal fins move, how the pectorals move, and the frame rate.

  caudal / dorsal / anal / pectoral / pelvic / adipose / barbel / ribbon : amplitude multipliers
  median : 'tips'   only the trailing tips of dorsal and anal flutter (streamlined swimmers)
           'whole'  the whole fin sways with the tail (rear-set fins: killifish, gar)
           'ripple' a ripple runs along the fin margin, strongest on the soft rear rays (cichlids, sunfish, catfish anal fin)
  tip : caudal weight exponent (>1: only the lobe tips flick; small darting fish)
  ripple_k : ripples along the fin;  pec : 'flap' (up-down) or 'row' (fore-and-aft sculling)
"""
P = {
    'dart':     dict(caudal=1.0, tip=3.0, dorsal=0.3, anal=0.3, median='tips', pectoral=0.2, pec='flap', pelvic=0.4, adipose=0.4, fps=10),
    'tetra':    dict(caudal=1.3, dorsal=1.5, anal=1.5, median='whole', pectoral=0.3, pec='row', pelvic=0.6, adipose=0.6, fps=10),
    'cruise':   dict(caudal=1.5, dorsal=0.45, anal=0.45, median='tips', pectoral=0.2, pec='flap', pelvic=0.5, adipose=0.5, fps=8),
    'power':    dict(caudal=1.9, dorsal=0.4, anal=0.4, median='tips', pectoral=0.0, pec='flap', pelvic=0.5, adipose=0.6, fps=9),
    'killi':    dict(caudal=1.4, dorsal=1.0, anal=1.0, median='whole', pectoral=0.4, pec='row', pelvic=0.5, fps=8),
    'hover':    dict(caudal=0.9, dorsal=0.9, anal=0.8, median='ripple', ripple_k=1.0, pectoral=1.3, pec='row', pelvic=0.6, adipose=0.4, fps=8),
    'sail':     dict(caudal=1.1, dorsal=1.7, anal=1.0, median='ripple', ripple_k=1.2, pectoral=0.4, pec='row', pelvic=0.5, fps=8),
    'darter':   dict(caudal=0.9, dorsal=0.5, anal=0.4, median='ripple', ripple_k=1.0, pectoral=1.0, pec='flap', pelvic=0.6, fps=8),
    'cichlid':  dict(caudal=1.1, dorsal=1.7, anal=1.7, median='ripple', ripple_k=1.5, pectoral=1.2, pec='row', pelvic=0.7, fps=7),
    'sunfish':  dict(caudal=1.0, dorsal=1.5, anal=1.5, median='ripple', ripple_k=1.3, pectoral=1.4, pec='row', pelvic=0.6, fps=7),
    'stalker':  dict(caudal=0.8, dorsal=1.3, anal=1.1, median='ripple', ripple_k=2.0, pectoral=0.6, pec='row', pelvic=0.4, fps=7),
    'gar':      dict(caudal=0.8, dorsal=1.0, anal=1.0, median='whole', pectoral=0.6, pec='row', pelvic=0.4, fps=5),
    'deep':     dict(caudal=1.1, dorsal=0.6, anal=0.6, median='tips', pectoral=0.6, pec='row', pelvic=0.5, adipose=0.4, fps=6),
    'catfish':  dict(caudal=0.9, dorsal=0.4, anal=1.0, median='ripple', ripple_k=1.5, pectoral=0.5, pec='row', pelvic=0.5, adipose=0.6, barbel=1.6, fps=6),
    'sturgeon': dict(caudal=1.2, dorsal=0.3, anal=0.3, median='tips', pectoral=0.3, pec='flap', pelvic=0.4, barbel=1.0, fps=5),
    'riffle':   dict(caudal=1.0, tip=1.6, dorsal=0.4, anal=0.4, median='tips', pectoral=0.9, pec='flap', pelvic=0.6, fps=10),
    'sucker':   dict(caudal=1.1, dorsal=0.5, anal=0.4, median='tips', pectoral=0.9, pec='flap', pelvic=0.7, fps=6),
    'eel':      dict(caudal=1.4, dorsal=1.3, anal=1.3, median='ripple', ripple_k=2.0, fps=8),
    'ribbon':   dict(caudal=0.4, dorsal=0.2, anal=0.2, median='tips', pectoral=0.5, pec='row', pelvic=0.3, ribbon=1.3, fps=8),
}
CS = {
    'coastal_shiner': 'dart', 'ironcolor_shiner': 'dart', 'tidewater_silverside': ('dart', dict(fps=11)),
    'buenos_aires_tetra': 'tetra', 'moenkhausia_bonita': 'tetra', 'yellowtail_lambari': ('cruise', dict(caudal=1.6, fps=10)),
    'spotted_pyrrhulina': 'hover', 'seminole_killifish': 'killi', 'florida_flagfish': ('killi', dict(median='ripple', ripple_k=1.2)),
    'sailfin_molly': 'sail', 'swamp_darter': 'darter',
    'banded_cichlid': 'cichlid', 'chanchito': 'cichlid', 'pike_cichlid': 'stalker',
    'redbreast_sunfish': 'sunfish', 'spotted_sunfish': 'sunfish', 'suwannee_bass': ('sunfish', dict(caudal=1.25, pectoral=0.7)),
    'lake_chubsucker': ('cruise', dict(caudal=1.2, fps=7)), 'three_spot_piau': 'cruise', 'striped_mullet': ('cruise', dict(fps=9)),
    'curimbata': 'cruise', 'common_snook': ('cruise', dict(caudal=1.3, fps=7)),
    'golden_dorado': ('power', dict(fps=8)), 'piraputanga': 'power', 'piracanjuba': ('power', dict(caudal=1.7)),
    'florida_gar': 'gar', 'pacu': 'deep', 'pintado': 'catfish', 'gulf_sturgeon': 'sturgeon', 'banded_knifefish': 'ribbon',
}
FS = {
    'blacknose_dace': 'riffle', 'longnose_dace': ('riffle', dict(pectoral=1.2, fps=9)), 'southern_redbelly_dace': 'dart',
    'rosyside_dace': ('cruise', dict(caudal=1.3, fps=10)), 'warpaint_shiner': 'tetra', 'saffron_shiner': 'dart', 'rosyface_shiner': ('dart', dict(fps=11)),
    'northern_studfish': 'killi', 'central_mudminnow': ('hover', dict(median='whole', dorsal=1.0, anal=1.0, fps=7)),
    'rainbow_darter': 'darter', 'greenside_darter': ('darter', dict(pectoral=1.3, fps=7)), 'redline_darter': ('darter', dict(fps=9)),
    'tangerine_darter': ('darter', dict(caudal=1.3, pectoral=0.6)), 'fantail_darter': ('darter', dict(dorsal=1.1, ripple_k=1.4)),
    'tessellated_darter': ('darter', dict(caudal=0.8, fps=7)),
    'central_stoneroller': ('cruise', dict(caudal=1.2)), 'bluehead_chub': 'cruise', 'creek_chub': ('cruise', dict(fps=9)),
    'fallfish': ('power', dict(caudal=1.6, fps=8)), 'american_shad': 'power',
    'northern_hog_sucker': 'sucker', 'white_sucker': ('sucker', dict(pectoral=0.5)), 'river_redhorse': ('sucker', dict(caudal=1.3, pectoral=0.4, fps=7)),
    'longear_sunfish': 'sunfish', 'rock_bass': ('sunfish', dict(caudal=1.1, fps=6)), 'smallmouth_bass': ('sunfish', dict(caudal=1.3, pectoral=0.7)),
    'logperch': ('darter', dict(caudal=1.1, pectoral=0.7)), 'walleye': ('stalker', dict(caudal=1.0, fps=6)), 'sauger': ('stalker', dict(caudal=1.0, ripple_k=1.6)),
    'muskellunge': 'gar', 'american_brook_lamprey': 'eel',
}
MS = {
    'european_bitterling': ('tetra', dict(caudal=1.2)), 'rosy_bitterling': ('tetra', dict(caudal=1.2)), 'sunbleak': ('dart', dict(fps=11)),
    'medaka': ('killi', dict(fps=9)), 'topmouth_gudgeon': ('cruise', dict(fps=10)), 'northern_redbelly_dace': 'dart',
    'three_spined_stickleback': ('hover', dict(caudal=0.8, pectoral=1.6, median='whole', fps=9)),
    'ninespine_stickleback': ('hover', dict(caudal=0.8, pectoral=1.6, median='whole', fps=9)),
    'okefenokee_pygmy_sunfish': ('sunfish', dict(fps=8)), 'blackbanded_sunfish': 'sunfish', 'bluespotted_sunfish': 'sunfish',
    'banded_killifish': 'killi', 'golden_shiner': ('cruise', dict(fps=9)), 'paradise_fish': 'cichlid', 'frog_tadpole': ('eel', dict(fps=10)),
    'crucian_carp': ('cruise', dict(caudal=1.2, fps=7)), 'rudd': 'cruise', 'tench': ('deep', dict(pectoral=0.8)),
    'european_perch': ('stalker', dict(caudal=1.0)), 'ruffe': ('stalker', dict(caudal=1.0, fps=8)), 'pumpkinseed': 'sunfish',
    'amur_sleeper': ('hover', dict(caudal=1.0, fps=7)), 'mandarin_fish': ('stalker', dict(fps=6)), 'black_bullhead': 'catfish',
    'grass_pickerel': 'gar', 'northern_pike': 'gar', 'asian_swamp_eel': 'eel', 'european_eel': 'eel',
    'northern_snakehead': ('stalker', dict(caudal=1.1, ripple_k=2.2, fps=6)), 'wels_catfish': ('catfish', dict(fps=5)),
}
TABLE = {'cs': CS, 'fs': FS, 'ms': MS}
def lookup(pre, name):
    e = TABLE.get(pre, {}).get(name)
    if e is None: return None
    if isinstance(e, str): return dict(P[e], name=e)
    g = dict(P[e[0]], name=e[0]); g.update(e[1]); return g
