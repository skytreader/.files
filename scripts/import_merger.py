#!/usr/bin/env python3

def normalize_imports(i):
    sans_breaks = " ".join([l.strip() for l in i.split("\n")])
    return set(sans_breaks.split(", "))

def merge_imports(i1, i2):
    ni1 = normalize_imports(i1)
    ni2 = normalize_imports(i2)
    return ", ".join(ni1 | ni2)
