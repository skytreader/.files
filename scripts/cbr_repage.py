#! /usr/bin/env python3
import glob
import os
import sys

"""
For CBR files whose pages are messed up because the filenames of the individual
pages are not done properly. This script will help you relabel the files.

Instructions: Extract the contents of the CBR archive in a directory of its own.
Then, give that directory to this script. If needed, rewrite the transform
function. After that, recompile CBR if need be.
"""

def transform(fname):
    """
    Transform the given filename to a string that will give it the right
    pagination.

    :fname - string. We expect a three-character file extension to be present.
    
    return another string.
    """
    print(fname)
    parse = fname[0:len(fname) - 4].split("-")
    return "0" + parse[1] + fname[-4:]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 %s <extracted_cbr_dir>" % (sys.argv[0]))
        exit(1)

    if sys.argv[1][-1] != "/":
        sys.argv[1] += "/"

    cbr_pages = glob.glob(sys.argv[1] + "*")
    print(cbr_pages)

    for page in cbr_pages:
        plain_name = page.split("/")[-1]
        transformed = transform(plain_name)
        os.rename(page, sys.argv[1] + transformed)
