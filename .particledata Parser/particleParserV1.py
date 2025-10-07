import struct, json, sys, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

print("===========Disney Infinity 3.0 .particledata parser============")
print("Made by Cassinni4")

class ParticleDataParser:
    FOOTER_MAGIC = b'\x23\x01'               # 0x0123 little-endian
    FOOTER_STRUCT = struct.Struct('<HHIIHHHHHH')  # 24 bytes

    PARTICLE_FILE_RECORD_STRUCT = struct.Struct('<IIHHI')  # offset, nameHash, priority, materialIndex, bucketPriority
    EFFECT_FILE_RECORD_STRUCT   = struct.Struct('<II')     # offset, nameHash
    EMITTER_FILE_RECORD_STRUCT  = struct.Struct('<II')     # offset, nameHash
    ENVELOPE_STRUCT             = struct.Struct('<BBBBBBBB') # 8-byte envelope struct
    LENSFLARE_FILE_RECORD_STRUCT = struct.Struct('<IIHH')   # offset, nameHash, materialIndex, unused
    LENSFLARE_ARRAY_FILE_RECORD_STRUCT = struct.Struct('<II') # offset, nameHash

    def __init__(self, data: bytes):
        self.data = data
        self.size = len(data)
        self.footer = None
        self.footer_offset = None
        self.particle_records = []
        self.effect_records = []
        self.emitter_records = []
        self.envelope_records = []
        self.lensflare_records = []
        self.lensflare_array_records = []

    def find_and_parse_footer(self):
        idx = self.data.rfind(self.FOOTER_MAGIC)
        if idx == -1:
            raise ValueError("Footer magic 0x0123 not found in file")
        if idx + self.FOOTER_STRUCT.size > self.size:
            raise ValueError("Not enough bytes after footer magic")
        fields = self.FOOTER_STRUCT.unpack_from(self.data, idx)
        self.footer_offset = idx
        self.footer = {
            'magic': fields[0],
            'version': fields[1],
            'keep_size': fields[2],
            'envelope_offset': fields[3],
            'envelope_count': fields[4],
            'particle_count': fields[5],
            'effect_count': fields[6],
            'emitter_count': fields[7],
            'lensflare_count': fields[8],
            'lensflare_array_count': fields[9],
        }
        logging.info(f"Footer parsed at {idx}, file size {self.size}")
        return self.footer

    def parse_file_records(self):
        if not self.footer:
            self.find_and_parse_footer()

        off = self.footer_offset

        # LensFlareArrayFileRecords
        count = self.footer['lensflare_array_count']
        size = self.LENSFLARE_ARRAY_FILE_RECORD_STRUCT.size * count
        off -= size
        self.lensflare_array_records = []
        for i in range(count):
            rec = self.LENSFLARE_ARRAY_FILE_RECORD_STRUCT.unpack_from(self.data, off + i * self.LENSFLARE_ARRAY_FILE_RECORD_STRUCT.size)
            self.lensflare_array_records.append({'offset': rec[0], 'nameHash': hex(rec[1])})
        logging.info(f"Read {len(self.lensflare_array_records)} lensflare array records")

        # LensFlareFileRecords
        count = self.footer['lensflare_count']
        size = self.LENSFLARE_FILE_RECORD_STRUCT.size * count
        off -= size
        self.lensflare_records = []
        for i in range(count):
            rec = self.LENSFLARE_FILE_RECORD_STRUCT.unpack_from(self.data, off + i * self.LENSFLARE_FILE_RECORD_STRUCT.size)
            self.lensflare_records.append({
                'offset': rec[0],
                'nameHash': hex(rec[1]),
                'materialIndex': rec[2],
                'unused': rec[3]
            })
        logging.info(f"Read {len(self.lensflare_records)} lensflare records")

        # EmitterFileRecords
        count = self.footer['emitter_count']
        size = self.EMITTER_FILE_RECORD_STRUCT.size * count
        off -= size
        self.emitter_records = []
        for i in range(count):
            rec = self.EMITTER_FILE_RECORD_STRUCT.unpack_from(self.data, off + i * self.EMITTER_FILE_RECORD_STRUCT.size)
            self.emitter_records.append({'offset': rec[0], 'nameHash': hex(rec[1])})
        logging.info(f"Read {len(self.emitter_records)} emitter records")

        # EffectFileRecords
        count = self.footer['effect_count']
        size = self.EFFECT_FILE_RECORD_STRUCT.size * count
        off -= size
        self.effect_records = []
        for i in range(count):
            rec = self.EFFECT_FILE_RECORD_STRUCT.unpack_from(self.data, off + i * self.EFFECT_FILE_RECORD_STRUCT.size)
            self.effect_records.append({'offset': rec[0], 'nameHash': hex(rec[1])})
        logging.info(f"Read {len(self.effect_records)} effect records")

        # ParticleFileRecords
        count = self.footer['particle_count']
        size = self.PARTICLE_FILE_RECORD_STRUCT.size * count
        off -= size
        self.particle_records = []
        for i in range(count):
            rec = self.PARTICLE_FILE_RECORD_STRUCT.unpack_from(self.data, off + i * self.PARTICLE_FILE_RECORD_STRUCT.size)
            self.particle_records.append({
                'offset': rec[0],
                'nameHash': hex(rec[1]),
                'priority': rec[2],
                'materialIndex': rec[3],
                'bucketPriority': rec[4]
            })
        logging.info(f"Read {len(self.particle_records)} particle records")

        return {
            'particles': self.particle_records,
            'effects': self.effect_records,
            'emitters': self.emitter_records,
            'lensflares': self.lensflare_records,
            'lensflare_arrays': self.lensflare_array_records
        }

    def parse_envelopes(self):
        if not self.footer:
            self.find_and_parse_footer()
        count = self.footer['envelope_count']
        offset = self.footer['envelope_offset']
        self.envelope_records = []
        for i in range(count):
            rec = self.ENVELOPE_STRUCT.unpack_from(self.data, offset + i * self.ENVELOPE_STRUCT.size)
            self.envelope_records.append({
                'point0Y': rec[0],
                'point1Y': rec[1],
                'point2Y': rec[2],
                'point3Y': rec[3],
                'point1X': rec[4],
                'point2X': rec[5],
                'floor': rec[6],
                'ceiling': rec[7]
            })
        logging.info(f"Read {len(self.envelope_records)} envelopes")
        return self.envelope_records

    def dump_summary(self):
        return {
            'footer': self.footer,
            'particle_records': self.particle_records,
            'effect_records': self.effect_records,
            'emitter_records': self.emitter_records,
            'lensflare_records': self.lensflare_records,
            'lensflare_array_records': self.lensflare_array_records,
            'envelope_records': self.envelope_records
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python particleParserV1.py <file.particledata> [--out output.json]")
        sys.exit(1)

    path = sys.argv[1]
    out_path = None
    if len(sys.argv) >= 4 and sys.argv[2] == "--out":
        out_path = sys.argv[3]

    data = Path(path).read_bytes()
    parser = ParticleDataParser(data)
    parser.find_and_parse_footer()
    parser.parse_file_records()
    parser.parse_envelopes()
    result = parser.dump_summary()

    if out_path:
        Path(out_path).write_text(json.dumps(result, indent=2))
        logging.info(f"JSON written to {out_path}")
    else:
        print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

print("===============================================================")