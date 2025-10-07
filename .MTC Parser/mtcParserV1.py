import sys
import struct
import json
import os

EXPECTED_MAGIC = 0x0000FFFF

def read_u32(data, offset, endian='<'):
    return struct.unpack_from(endian + 'I', data, offset)[0]

def read_null_terminated(data, offset):
    if offset < 0 or offset >= len(data):
        return None
    end = data.find(b'\x00', offset)
    if end == -1:
        return data[offset:].decode('utf-8', errors='replace')
    return data[offset:end].decode('utf-8', errors='replace')

def fnv1a_hash32(s: str) -> int:
    # Compute FNV-1a 32-bit hash of a string (same as Hash32 in engine).
    fnv_prime = 0x01000193
    hval = 0x811c9dc5
    for c in s.encode("utf-8"):
        hval ^= c
        hval = (hval * fnv_prime) & 0xffffffff
    return hval

def parse_mtc(path):
    with open(path, 'rb') as f:
        data = f.read()

    if len(data) < 12:
        return {'error': 'File too small to contain valid .MTC header', 'filesize': len(data)}

    magic_le = struct.unpack_from('<I', data, 0)[0]
    magic_be = struct.unpack_from('>I', data, 0)[0]

    if magic_le == EXPECTED_MAGIC:
        endian = '<'
    elif magic_be == EXPECTED_MAGIC:
        endian = '>'
    elif magic_le == 0xFFFF0000:
        endian = '>'
    else:
        endian = '<'

    magic = read_u32(data, 0, endian)
    node_count = read_u32(data, 4, endian)
    link_count = read_u32(data, 8, endian)
    total_entries = node_count + link_count

    entries = []
    for i in range(total_entries):
        entry_offset = 12 + i * 8
        if entry_offset + 8 > len(data):
            entries.append({'count': None, 'offset': None})
            continue
        cnt = read_u32(data, entry_offset, endian)
        off = read_u32(data, entry_offset + 4, endian)
        entries.append({'count': cnt, 'offset': off})

    result_nodes, result_links = [], []

    for i, e in enumerate(entries):
        off = e['offset']
        name = None
        if off and off < len(data):
            name = read_null_terminated(data, off)

        hashedName = None
        hash32 = None
        if name:
            hashedName = f"MNode::{name}"
            hash32 = fnv1a_hash32(hashedName)

        row = {
            'index': i,
            'count': e['count'],
            'offset': off,
            'name': name,
            'hashedName': hashedName,
            'hash32': hash32
        }

        if i < node_count:
            result_nodes.append(row)
        else:
            result_links.append(row)

    return {
        'file': os.path.basename(path),
        'filesize': len(data),
        'detected_endian': 'little' if endian == '<' else 'big',
        'magic': magic,
        'nodeCount': node_count,
        'linkCount': link_count,
        'totalEntries': total_entries,
        'nodes': result_nodes,
        'links': result_links,
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mctParserV1.py file.mtc [out.json]", file=sys.stderr)
        sys.exit(1)

    mtc_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None

    parsed = parse_mtc(mtc_path)
    if out_path:
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(parsed, f, indent=2, ensure_ascii=False)
    else:
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
