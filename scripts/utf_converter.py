#! /usr/bin/env python3

import codecs
import sys

"""
Converts a UTF-16 file to UTF-8.
"""

if __name__ == "__main__":
    with codecs.open(sys.argv[1], "rb", "utf-16") as utf16_file:
        with codecs.open(sys.argv[2], "wb", "utf-8") as utf8_file:
            utf8_file.write(utf16_file.read())
