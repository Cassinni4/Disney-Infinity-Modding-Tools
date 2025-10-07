#BUILDDATE 9/25/25

import argparse

# GATEWAY IS DONE RAHHHHHHHHHHHHHHHHHHHHH
# cass

def stringToLuaHex(hex_str: str) -> str:
    raw_bytes = bytes.fromhex(hex_str)
    return ''.join(f'\\{b:03d}' for b in raw_bytes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert hex string to Lua-style decimal escape sequence.")
    parser.add_argument("hex_string", help="Hex string to convert")
    args = parser.parse_args()

    result = stringToLuaHex(args.hex_string)
    print(result)
