#! /usr/bin/env python3

import codecs
import sys

"""
Converts a UTF-16 file to UTF-8.

TODO Maybe make this invokable from anywhere?
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s utf16_source utf8_target" % sys.argv[0])
        exit(1)

    source = sys.argv[1]
    dest = sys.argv[2]

    with codecs.open(source, "rb", "utf-16") as utf16_file:
        with codecs.open(dest, "wb", "utf-8") as utf8_file:
            utf8_file.write(utf16_file.read())
