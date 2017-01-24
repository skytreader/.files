#! /usr/bin/env python3

import sys

"""
Remove all useless characters in strings.
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python %s dirty clean" % sys.argv[0])

    source = sys.argv[1]
    src = []

    with open(source, "rb") as source_:
        source_byte = source_.read(1)
        progress_counter = 0
        while source_byte != b"":
            byteint = int.from_bytes(source_byte, byteorder="big")
            if 32 <= byteint <= 126 or byteint == 10:
                src.append(chr(byteint))
            source_byte = source_.read(1)

    dest = sys.argv[2]

    with open(dest, "w") as dest_:
        dest_.write("".join(src))
