"""
BCTParser.py
- Heuristically analyzes binary .bct files (attempts to reconstruct LinkNames, Filters, Mirrors).
Usage:
    python BCTParser.py file.bct
Outputs:
  - <basename>_tup_ascii.json  (if ascii parsed)
  - <basename>_parsed_summary.json
  - <basename>_filters.json
  - <basename>_mirrors.json
"""
import sys, os, re, json, struct

# --------------------
# ASCII Tupperware parser (apparently these exist, not in in3 however)
# --------------------
token_re = re.compile(r'\s*([A-Za-z_][A-Za-z0-9_]*)\s*(?:"([^"]*)")?\s*=\s*', re.MULTILINE)

def parse_ascii_value(s, i=0):
    # Skip whitespace
    L = len(s)
    while i < L and s[i].isspace():
        i += 1
    if i >= L:
        return None, i
    if s[i] == '{':
        # aggregate
        i += 1
        agg = []
        while True:
            # skip whitespace
            while i < L and s[i].isspace():
                i += 1
            if i < L and s[i] == '}':
                i += 1
                break
            m = token_re.match(s, i)
            if not m:
                # no key => break
                break
            key = m.group(1)
            name = m.group(2)
            i = m.end()
            val, i = parse_ascii_value(s, i)
            agg.append( (key, name, val) )
        return agg, i
    elif s[i] == '[':
        # list
        i += 1
        items = []
        token = ''
        in_str = False
        while i < L:
            ch = s[i]
            if in_str:
                if ch == '"':
                    in_str = False
                    items.append(token)
                    token = ''
                else:
                    token += ch
                i += 1
                continue
            if ch.isspace():
                i += 1
                continue
            if ch == ']':
                i += 1
                break
            if ch == '"':
                in_str = True
                i += 1
                continue
            # otherwise parse number-like token until whitespace or ]
            j = i
            while j < L and not s[j].isspace() and s[j] != ']':
                j += 1
            tok = s[i:j]
            # try int then float
            try:
                if '.' in tok or 'e' in tok or 'E' in tok:
                    val = float(tok)
                else:
                    val = int(tok)
            except Exception:
                val = tok
            items.append(val)
            i = j
        return items, i
    else:
        # scalar: string or number
        # if starts with quote
        if s[i] == '"':
            i += 1
            j = i
            while j < L and s[j] != '"':
                j += 1
            val = s[i:j]
            return val, j+1
        # otherwise parse until newline or semicolon or close brace
        j = i
        while j < L and s[j] not in "\r\n":
            j += 1
        tok = s[i:j].strip()
        # try parse as float or int
        try:
            if '.' in tok or 'e' in tok or 'E' in tok:
                return float(tok), j
            else:
                return int(tok), j
        except Exception:
            return tok, j

def parse_ascii_tupperware(text):
    # find top-level key/value pairs or aggregates
    pos = 0
    L = len(text)
    root = []
    while True:
        m = token_re.search(text, pos)
        if not m:
            break
        key = m.group(1)
        name = m.group(2)
        pos = m.end()
        val, pos = parse_ascii_value(text, pos)
        root.append((key, name, val))
    return root

# --------------------
# Binary heuristics parser (what seems to be used in the game)
# --------------------
def extract_printable_strings(blob, min_len=3):
    res = []
    cur = []
    for b in blob:
        if 32 <= b <= 126:
            cur.append(chr(b))
        else:
            if len(cur) >= min_len:
                res.append(''.join(cur))
            cur = []
    if len(cur) >= min_len:
        res.append(''.join(cur))
    return res

def find_all_subbytes(blob, token):
    t = token.encode('ascii')
    i = 0
    out = []
    while True:
        pos = blob.find(t, i)
        if pos == -1:
            break
        out.append(pos)
        i = pos + 1
    return out

# scan for 32-bit floats sequences within window
def scan_float_sequences(blob, pos, window=4096, min_len=4):
    start = max(0, pos - window)
    end = min(len(blob), pos + window)
    data = blob[start:end]
    seqs = []
    for offset in range(0, len(data)-4, 4):
        floats = []
        for j in range(offset, len(data)-4, 4):
            f = struct.unpack_from('<f', data, j)[0]
            # Very permissive range but weed out NaN/inf
            if not (abs(f) < 1e10):
                break
            floats.append(f)
            if len(floats) >= min_len:
                # continue to extend to capture longer sequences
                continue
        if len(floats) >= min_len:
            seqs.append( (start + offset, floats) )
    # dedupe and sort by length
    seqs.sort(key=lambda x: -len(x[1]))
    dedup = {}
    for s, fl in seqs:
        if s not in dedup or len(fl) > len(dedup[s]):
            dedup[s] = fl
    return sorted([(s,dedup[s]) for s in dedup], key=lambda x: -len(x[1]))

def scan_uint32_sequences(blob, pos, window=4096, min_len=4):
    start = max(0, pos - window)
    end = min(len(blob), pos + window)
    data = blob[start:end]
    seqs = []
    for offset in range(0, len(data)-4, 4):
        us = []
        for j in range(offset, len(data)-4, 4):
            u = struct.unpack_from('<I', data, j)[0]
            us.append(u)
            if len(us) >= min_len:
                continue
        if len(us) >= min_len:
            seqs.append((start+offset, us))
    seqs.sort(key=lambda x: -len(x[1]))
    dedup = {}
    for s, us in seqs:
        if s not in dedup or len(us) > len(dedup[s]):
            dedup[s] = us
    return sorted([(s,dedup[s]) for s in dedup], key=lambda x: -len(x[1]))

def decode_mirror_value(u):
    # assume top 2 bits are flags, lower 30 bits index (common pattern)
    FLAGS_SHIFT = 30
    FLAGS_MASK = 3 << FLAGS_SHIFT
    INDEX_MASK = (1 << FLAGS_SHIFT) - 1
    flags = (u & FLAGS_MASK) >> FLAGS_SHIFT
    index = u & INDEX_MASK
    return index, flags

# --------------------
# Main
# --------------------
def main(path):
    base = os.path.splitext(os.path.basename(path))[0]
    with open(path, 'rb') as f:
        blob = f.read()
    # Quick ascii detection: presence of patterns like " = {" or KEY tokens.
    text_like = False
    try:
        txt = blob.decode('utf-8', errors='ignore')
    except:
        txt = ''
    if re.search(r'[A-Za-z_][A-Za-z0-9_]*\s*(?:"[^"]*")?\s*=\s*[{[]"]', txt):
        text_like = True

    summary = {
        "file": path,
        "size_bytes": len(blob),
        "ascii_detected": text_like
    }

    if text_like:
        root = parse_ascii_tupperware(txt)
        with open(base + '_tup_ascii.json', 'w', encoding='utf-8') as out:
            json.dump(root, out, indent=2, ensure_ascii=False)
        summary['ascii_parsed'] = True
        summary['ascii_root_top_count'] = len(root)
        print("[*] ASCII Tupperware parsed, wrote:", base + '_tup_ascii.json')
    else:
        summary['ascii_parsed'] = False
        # Extract printable strings
        strings = extract_printable_strings(blob, min_len=3)
        summary['strings_found'] = len(strings)
        print("[*] extracted {} ascii-like strings".format(len(strings)))

        # Try to locate LinkNames (exact token 'LinkNames' often used)
        link_names = []
        if 'LinkNames' in strings:
            offsets = find_all_subbytes(blob, 'LinkNames')
            # for each occurrence, collect following short strings in the window
            for pos in offsets:
                window = 4096
                start = pos
                end = min(len(blob), pos + window)
                cur = []
                names = []
                for i in range(start, end):
                    b = blob[i]
                    if 32 <= b <= 126:
                        cur.append(chr(b))
                    else:
                        if cur:
                            s = ''.join(cur)
                            if 0 < len(s) < 80 and ' ' not in s:
                                names.append(s)
                            cur = []
                if names:
                    link_names.extend(names)
        # fallback: pick many short candidate strings (likely bone/link names)
        if not link_names:
            for s in strings:
                if 1 < len(s) < 40 and ( '_' in s or s[0].isalpha() and s[0].isupper() or s.islower() ):
                    link_names.append(s)
            # keep unique
            seen = set()
            link_names = [x for x in link_names if not (x in seen or seen.add(x))]
        summary['link_names_guess_count'] = len(link_names)
        summary['link_names_sample'] = link_names[:200]

        # Find filters by scanning for prioritized strings and scanning floats nearby
        prioritized = [s for s in strings if any(tok in s.lower() for tok in ['filter','carry','weapon','lightsaber','upperbody','head','run','fire','throw','mirror'])]
        # also include a few top strings
        prioritized += strings[:200]
        filters = {}
        name_offsets = {s: find_all_subbytes(blob, s) for s in set(strings)}
        for name in prioritized:
            offs = name_offsets.get(name, [])
            for pos in offs:
                float_seqs = scan_float_sequences(blob, pos, window=4096, min_len= max(4, len(link_names)//8 if link_names else 4))
                if float_seqs:
                    s0, fls = float_seqs[0]
                    # heuristics: prefer sequences similar to link_names length
                    if link_names and abs(len(fls) - len(link_names)) <= max(1, int(0.1*len(link_names))):
                        filters[name] = fls
                        break
                    if name not in filters:
                        filters[name] = fls
                        break
            if len(filters) >= 200:
                break

        # Mirrors: scan for uint32 sequences near 'Mirror' tokens
        mirrors = {}
        mirror_candidates = [s for s in strings if 'mirror' in s.lower()]
        mirror_candidates += strings[:100]
        for name in mirror_candidates:
            offs = name_offsets.get(name, [])
            for pos in offs:
                u_seqs = scan_uint32_sequences(blob, pos, window=4096, min_len=4)
                if u_seqs:
                    s0, us = u_seqs[0]
                    decoded = [ decode_mirror_value(u) for u in us ]
                    mirrors[name] = decoded
                    break
            if len(mirrors) >= 200:
                break

        # Write outputs
        with open(base + '_parsed_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        with open(base + '_filters.json', 'w', encoding='utf-8') as f:
            # convert floats to shorter formatting to keep file small
            jsf = {k: [ float("%.6g"%v) for v in (vals if isinstance(vals, list) else vals) ] for k,vals in filters.items()}
            json.dump(jsf, f, indent=2)
        with open(base + '_mirrors.json', 'w', encoding='utf-8') as f:
            jsm = {k: [ {"index": i, "flags": fl} for (i,fl) in v ] for k,v in mirrors.items()}
            json.dump(jsm, f, indent=2)

        print("[*] heuristic binary parse complete.")
        print("    link_names_guess_count:", summary['link_names_guess_count'])
        print("    filters_found:", len(filters))
        print("    mirrors_found:", len(mirrors))
        print("    wrote:", base + "_parsed_summary.json,", base + "_filters.json,", base + "_mirrors.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python BCTParser.py file.bct")
        sys.exit(1)
    main(sys.argv[1])
