import os
import struct
import sys
import numpy as np

# Usage: python objConverterV3.py model.obj
# Add "--extended" to the end of the command if you want extra debug information
# INSTALL NUMPY GOOFBALL

# Flag for --extended
extended = ('--extended' in sys.argv)

# Determine .OBJ filename while preserving original behavior
objFilename = sys.argv[1]
if objFilename == '--extended' and len(sys.argv) > 2:
    objFilename = sys.argv[2]

base = os.path.splitext(objFilename)[0]
ibufFilename = base + ".ibuf"
vbufFilename = base + ".vbuf"

vertices = []      # list[(x,y,z)]
uvs = []           # list[(u,v)]
faces = []         # list[ ( (v1,vt1), (v2,vt2), (v3,vt3) ) ]  (0-based)

# Helper to print only in extended mode
_ext_count = {
    'v': 0,
    'vt': 0,
    'f': 0,
}

def EXT(msg):
    if extended:
        print(msg)

print("===========Disney Infinity 3.0 Gold Edition Model Converter============")
print("Made by Cassinni4 and Eidan Yoson")
print("[INFO] Starting conversion process")
print("[INFO] Reading .OBJ file")
file_length_in_bytes = os.path.getsize(objFilename)
print(f"[INFO] {objFilename} size: {file_length_in_bytes} bytes")
EXT(f"[EXT] Opening .OBJ: {objFilename}")

with open(objFilename, 'r', encoding='utf-8', errors='ignore') as f:
    for line_num, line in enumerate(f, start=1):
        if line.startswith('v '):
            parts = line.strip().split()
            _, xs, ys, zs = parts[:4]
            x, y, z = float(xs), float(ys), float(zs)
            vertices.append((x, y, z))
            _ext_count['v'] += 1
            EXT(f"[EXT] line {line_num}: VERTEX #{_ext_count['v']} -> x={x}, y={y}, z={z}")
        elif line.startswith('vt '):
            parts = line.strip().split()
            # Some OBJs have only u or have extra components; guard it
            u = float(parts[1])
            v = float(parts[2]) if len(parts) > 2 else 0.0
            uvs.append((u, v))
            _ext_count['vt'] += 1
            EXT(f"[EXT] line {line_num}: UV #{_ext_count['vt']} -> u={u}, v={v}")
        elif line.startswith('f '):
            parts = line.strip().split()[1:]
            # Expect triangles; if quads appear, you can triangulate, but we’ll assume tris here.
            if len(parts) != 3:
                raise ValueError("Non-triangle face found; triangulate your .OBJ first.")
            corner_pairs = []
            for corner_idx, p in enumerate(parts):
                # Supports f v/vt or v/vt/vn or v//vn; vt may be missing
                bits = p.split('/')
                v_idx = int(bits[0]) - 1
                vt_idx = int(bits[1]) - 1 if len(bits) > 1 and bits[1] != '' else None
                corner_pairs.append((v_idx, vt_idx))
                EXT(f"[EXT] line {line_num}: FACE corner {corner_idx} -> v={v_idx}, vt={vt_idx}")
            faces.append(tuple(corner_pairs))
            _ext_count['f'] += 1
            EXT(f"[EXT] line {line_num}: FACE #{_ext_count['f']} -> {corner_pairs}")
        else:
            # Non-geometry lines are ignored, but still trace in extended mode
            EXT(f"[EXT] line {line_num}: Ignored -> {line.rstrip()}")

print(f"[INFO] Finished parsing .OBJ")
print(f"[INFO] UVs parsed: {len(uvs)}")
print(f"[INFO] Vertices parsed: {len(vertices)}")
print(f"[INFO] Polygons parsed: {len(faces)}")
EXT(f"[EXT] Parse summary -> vertices={len(vertices)}, uvs={len(uvs)}, faces(tris)={len(faces)}")

# -----------------------
# Write .ibuf (triangle vertex indices as shorts)
# -----------------------
print("[INFO] Writing .IBUF file")
with open(ibufFilename, "wb") as ibuf_File:
    for i, tri in enumerate(faces):
        v1, v2, v3 = (tri[0][0], tri[1][0], tri[2][0])
        packed = struct.pack('<hhh', v1, v2, v3)
        ibuf_File.write(packed)
        if i % 1000 == 0 and i > 0:
            print(f"[DEBUG] Processed {i} triangles for .IBUF")
        EXT(f"[EXT] .IBUF tri #{i}: (v1={v1}, v2={v2}, v3={v3}) -> bytes={packed.hex()}")

print(f"[INFO] .IBUF file written: {ibufFilename}")
try:
    _s = os.path.getsize(ibufFilename)
    EXT(f"[EXT] .IBUF size: {_s} bytes")
except Exception as _e:
    EXT(f"[EXT] .IBUF size check failed: {_e}")

# -----------------------
# Build vertex->UV map (first seen)
# -----------------------
print("[INFO] Building vertex-to-UV map")
vertex_to_uv = {}  # vertex index -> uv index
for face_idx, tri in enumerate(faces):
    for corner_idx, (v_i, vt_i) in enumerate(tri):
        if vt_i is not None and v_i not in vertex_to_uv:
            vertex_to_uv[v_i] = vt_i
            EXT(f"[EXT] map add: vertex {v_i} -> uv {vt_i} (from face #{face_idx}, corner {corner_idx})")

print(f"[INFO] Vertex-to-UV mappings created: {len(vertex_to_uv)}")
EXT(f"[EXT] First-appearance vertex->uv mappings detail: {vertex_to_uv}")

# Prepare per-vertex UVs (fallback to (0,0) if not mapped)
print("[INFO] Preparing per-vertex UVs")
per_vertex_uv = []
for i in range(len(vertices)):
    if i in vertex_to_uv and 0 <= vertex_to_uv[i] < len(uvs):
        per_vertex_uv.append(uvs[vertex_to_uv[i]])
        EXT(f"[EXT] per-vertex uv[{i}] -> source uv index {vertex_to_uv[i]} value={uvs[vertex_to_uv[i]]}")
    else:
        per_vertex_uv.append((0.0, 0.0))
        EXT(f"[EXT] per-vertex uv[{i}] -> default (0.0, 0.0) (no mapping)")

print("[INFO] Per-vertex UVs prepared")

# -----------------------
# Write .vbuf
# Format assumed: [float x][float y][float z][half u][half v] per vertex
# followed by 16 bytes of zero padding per vertex (unknown block)
# -----------------------
print("[INFO] Writing .VBUF file")
with open(vbufFilename, "wb") as vbuf_File:
    # Vertex blocks
    for i, ((x, y, z), (u, v)) in enumerate(zip(vertices, per_vertex_uv)):
        # Flip V to match common .OBJ->engine convention
        v_flipped = 1.0 - v
        xyz_bytes = struct.pack('<fff', x, y, z)
        u_half = np.float16(u)
        v_half = np.float16(v_flipped)
        vbuf_File.write(xyz_bytes)
        vbuf_File.write(u_half.tobytes())
        vbuf_File.write(v_half.tobytes())

        if i % 1000 == 0 and i > 0:
            print(f"[DEBUG] Processed {i} vertices for .VBUF")
        EXT(f"[EXT] .VBUF vert #{i}: x={x}, y={y}, z={z} | u={u} -> half={u_half.view(np.uint16):#06x}, v(1-v)={v_flipped} -> half={v_half.view(np.uint16):#06x} | xyz_bytes={xyz_bytes.hex()}")

    # Per-vertex trailing padding: real zero bytes
    zero16 = b'\x00' * 16
    for i in range(len(vertices)):
        vbuf_File.write(zero16)
        EXT(f"[EXT] .VBUF pad block for vertex #{i}: {zero16.hex()}")

print(f"[INFO] .VBUF file written: {vbufFilename}")
try:
    _s = os.path.getsize(vbufFilename)
    EXT(f"[EXT] .VBUF size: {_s} bytes")
except Exception as _e:
    EXT(f"[EXT] .VBUF size check failed: {_e}")
    
# -----------------------
# Write .oct
# -----------------------
#Temporary mockup for now, don't uncomment it.

#print("[INFO] Writing .OCT file")

#octFilename = base + ".oct"

#with open(octFilename, "w", encoding="utf-8") as oct_File:
    #oct_File.write('<?xml version="1.0" encoding="UTF-8"?>\n')


#print(f"[INFO] .OCT file written: {octFilename}")


print("[INFO] Conversion process finished successfully.")
print("[INFO] Make sure you have the BONELESS .OCT file!")
print("[INFO] If the model errors, contact Cassinni4 on Discord.")
print("===================================================================")
