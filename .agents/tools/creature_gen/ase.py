"""Minimal Aseprite (.aseprite) writer: RGBA, one layer, one cel per frame, one tag per row. Written from the file-format spec."""
import struct, zlib, numpy as np
def _s(s): b = s.encode(); return struct.pack('<H', len(b)) + b
def _chunk(t, data): return struct.pack('<IH', len(data) + 6, t) + data
def write(path, sheet, W, H, tags, cols=4, dur=120, layer='Layer 1'):
    sheet = np.asarray(sheet, np.uint8); rows = sheet.shape[0] // H
    frames = []
    for r in range(rows):
        for c in range(cols): frames.append(sheet[r * H:(r + 1) * H, c * W:(c + 1) * W])
    cols_used = []
    for f in frames:
        for p in f.reshape(-1, 4):
            if p[3] and tuple(p) not in cols_used and len(cols_used) < 256: cols_used.append(tuple(p))
    body = b''
    for i, f in enumerate(frames):
        ch = []
        if i == 0:
            ch.append(_chunk(0x2007, struct.pack('<HHI', 1, 0, 0) + b'\0' * 8))
            pal = struct.pack('<III', max(1, len(cols_used)), 0, max(0, len(cols_used) - 1)) + b'\0' * 8
            for p in cols_used or [(0, 0, 0, 255)]: pal += struct.pack('<HBBBB', 0, *[int(v) for v in p])
            ch.append(_chunk(0x2019, pal))
            ch.append(_chunk(0x2004, struct.pack('<HHHHHHB3s', 3, 0, 0, 0, 0, 0, 255, b'\0' * 3) + _s(layer)))
            tg = struct.pack('<H8s', len(tags), b'\0' * 8)
            for k, name in enumerate(tags):
                tg += struct.pack('<HHBH6s3sB', k * cols, k * cols + cols - 1, 0, 0, b'\0' * 6, bytes((90, 170, 220)), 0) + _s(name)
            ch.append(_chunk(0x2018, tg))
        img = zlib.compress(np.ascontiguousarray(f).tobytes())
        ch.append(_chunk(0x2005, struct.pack('<HhhBHh5sHH', 0, 0, 0, 255, 2, 0, b'\0' * 5, W, H) + img))
        data = b''.join(ch)
        body += struct.pack('<IHHH2sI', len(data) + 16, 0xF1FA, min(len(ch), 0xFFFF), dur, b'\0\0', len(ch)) + data
    hdr = struct.pack('<IHHHHHIHIIB3sHBBhhHH84s', 128 + len(body), 0xA5E0, len(frames), W, H, 32, 1, dur, 0, 0, 0, b'\0' * 3, 0, 1, 1, 0, 0, 16, 16, b'\0' * 84)
    assert len(hdr) == 128
    open(path, 'wb').write(hdr + body)
def read(path):
    """parse back (for verification): returns W,H,n_frames,tags,frames list."""
    d = open(path, 'rb').read(); size, magic, nf, W, H, depth = struct.unpack_from('<IHHHHH', d, 0); assert magic == 0xA5E0
    off = 128; frames = []; tags = []
    for _ in range(nf):
        fb, fm, _o, dur, _z, nch = struct.unpack_from('<IHHH2sI', d, off); assert fm == 0xF1FA; p = off + 16
        for _c in range(nch):
            cs, ct = struct.unpack_from('<IH', d, p)
            if ct == 0x2005:
                w, h = struct.unpack_from('<HH', d, p + 6 + 16); frames.append(np.frombuffer(zlib.decompress(d[p + 6 + 20:p + cs]), np.uint8).reshape(h, w, 4))
            if ct == 0x2018:
                n = struct.unpack_from('<H', d, p + 6)[0]; q = p + 6 + 10
                for _t in range(n):
                    a, b = struct.unpack_from('<HH', d, q); q += 17; ln = struct.unpack_from('<H', d, q)[0]; tags.append((d[q + 2:q + 2 + ln].decode(), a, b)); q += 2 + ln
            p += cs
        off += fb
    return W, H, nf, tags, frames
