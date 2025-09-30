# BUILDDATE 9/30/25

import os
import sys
import struct
import numpy as np
import trimesh
import subprocess

# Usage: python gltfConverterV1.py model.gltf
# it will automatically find the .BIN if there is one!
# Add "--extended" to the end of the command if you want extra debug information
# INSTALL NUMPY GOOFBALL
# INSTALL TRIMESH GOOFBALL

extended = ("--extended" in sys.argv)

# Determine glTF filename
gltfFilename = sys.argv[1]
if gltfFilename == "--extended" and len(sys.argv) > 2:
    gltfFilename = sys.argv[2]

base = os.path.splitext(gltfFilename)[0]
ibufFilename = base + ".ibuf"
vbufFilename = base + ".vbuf"

def EXT(msg):
    if extended:
        print(msg)

print("===========Disney Infinity 3.0 Gold Edition Model Converter============")
print("Made by Cassinni4, Eidan Yoson, and HeyItsDuke")
print("[INFO] Starting conversion process")
print(f"[INFO] Reading .glTF file: {gltfFilename}")

# Load glTF into a mesh
scene = trimesh.load(gltfFilename, force='scene')
if not isinstance(scene, trimesh.Scene):
    scene = trimesh.Scene([scene])

# Merge meshes into one
mesh = scene.to_geometry()

vertices = mesh.vertices.tolist()
faces = mesh.faces.tolist()

# Handle UVs safely
if hasattr(mesh.visual, "uv") and mesh.visual.uv is not None:
    uvs = mesh.visual.uv.tolist()
else:
    uvs = []

print(f"[INFO] Vertices parsed: {len(vertices)}")
print(f"[INFO] Polygons parsed: {len(faces)}")
print(f"[INFO] UVs parsed: {len(uvs)}")

# -----------------------
# Write .IBUF
# -----------------------
print("[INFO] Writing .IBUF file")
with open(ibufFilename, "wb") as ibuf_File:
    for i, tri in enumerate(faces):
        v1, v2, v3 = tri
        packed = struct.pack("<hhh", v1, v2, v3)
        ibuf_File.write(packed)
        if i % 1000 == 0 and i > 0:
            print(f"[DEBUG] Processed {i} triangles for .IBUF")
        EXT(f"[EXT] .IBUF tri #{i}: (v1={v1}, v2={v2}, v3={v3}) -> {packed.hex()}")

print(f"[INFO] .IBUF file written: {ibufFilename}")

# -----------------------
# Per-vertex UVs
# -----------------------
print("[INFO] Preparing per-vertex UVs")
per_vertex_uv = []
for i in range(len(vertices)):
    if i < len(uvs):
        u, v = uvs[i]
        per_vertex_uv.append((u, v))
        EXT(f"[EXT] per-vertex uv[{i}] -> u={u}, v={v}")
    else:
        per_vertex_uv.append((0.0, 0.0))
        EXT(f"[EXT] per-vertex uv[{i}] -> default (0.0, 0.0)")

print("[INFO] Per-vertex UVs prepared")

# -----------------------
# Write .VBUF
# -----------------------
print("[INFO] Writing .VBUF file")
with open(vbufFilename, "wb") as vbuf_File:
    for i, ((x, y, z), (u, v)) in enumerate(zip(vertices, per_vertex_uv)):
        v_flipped = 1.0 - v
        xyz_bytes = struct.pack("<fff", x, y, z)
        u_half = np.float16(u)
        v_half = np.float16(v_flipped)
        vbuf_File.write(xyz_bytes)
        vbuf_File.write(u_half.tobytes())
        vbuf_File.write(v_half.tobytes())
        EXT(f"[EXT] .VBUF vert #{i}: ({x},{y},{z}) | u={u}, v={v}")

    zero16 = b"\x00" * 16
    for i in range(len(vertices)):
        vbuf_File.write(zero16)
        EXT(f"[EXT] .VBUF pad block for vertex #{i}")

print(f"[INFO] .VBUF file written: {vbufFilename}")

# -----------------------
# OCTCreator.py
# -----------------------

# It works now. This will be heavily modified later probably, but good enough for now

print("[INFO] Launching OCTCreator.py with generated filenames")
print(f"[INFO] IBUF: {ibufFilename}")
print(f"[INFO] VBUF: {vbufFilename}")

# Did you download it?
if os.path.exists("OCTCreator.py"):
    try:
        # Do it
        result = subprocess.run([
            sys.executable, "OCTCreator.py", 
            f"--ibuf={ibufFilename}", 
            f"--vbuf={vbufFilename}",
            f"--base={base}"
        ], capture_output=True, text=True)
        
        print("[INFO] OCTCreator.py output:")
        print(result.stdout)
        if result.stderr:
            print("[WARNING] OCTCreator.py errors:")
            print(result.stderr)
            
    except Exception as e:
        print(f"[ERROR] Failed to run OCTCreator.py: {e}")
else:
    print("[WARNING] OCTCreator.py not found in current directory")
    print("[INFO] You'll need to run OCTCreator.py manually with the generated files")

print("[INFO] Conversion process finished successfully.")
print("===================================================================")