"""Write Godot 4 texture .import files for new sheets (same layout the editor writes: md5 of the res:// path in the cache name,
a fresh random uid, the project's 2D pixel-art texture params) so they can be committed together with the PNGs."""
import sys, os, glob, hashlib, secrets
CH = 'abcdefghijklmnopqrstuvwxy012345678'   # Godot ResourceUID alphabet (no z, no 9)
def uid():
    n = secrets.randbits(63); s = ''
    while True:
        s = CH[n % 34] + s; n //= 34
        if n == 0: return 'uid://' + s
T = '''[remap]

importer="texture"
type="CompressedTexture2D"
uid="{uid}"
path="res://.godot/imported/{name}-{h}.ctex"
metadata={{
"vram_texture": false
}}

[deps]

source_file="{res}"
dest_files=["res://.godot/imported/{name}-{h}.ctex"]

[params]

compress/mode=0
compress/high_quality=false
compress/lossy_quality=0.7
compress/uastc_level=0
compress/rdo_quality_loss=0.0
compress/hdr_compression=1
compress/normal_map=0
compress/channel_pack=0
mipmaps/generate=false
mipmaps/limit=-1
roughness/mode=0
roughness/src_normal=""
process/channel_remap/red=0
process/channel_remap/green=1
process/channel_remap/blue=2
process/channel_remap/alpha=3
process/fix_alpha_border=true
process/premult_alpha=false
process/normal_map_invert_y=false
process/hdr_as_srgb=false
process/hdr_clamp_exposure=false
process/size_limit=0
detect_3d/compress_to=1
'''
import paths; root = paths.REPO + '/'; n = 0
for d in sys.argv[1:]:
    for p in sorted(glob.glob(os.path.join(root, d, '*_4f.png'))):
        if os.path.exists(p + '.import'): continue
        res = 'res://' + os.path.relpath(p, root).replace(os.sep, '/'); name = os.path.basename(p)
        open(p + '.import', 'w', newline='\n').write(T.format(uid=uid(), name=name, h=hashlib.md5(res.encode()).hexdigest(), res=res)); n += 1
print('wrote', n, '.import files')
