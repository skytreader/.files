#!/usr/bin/env python3
"""
Construct guitar TABlature from an input language. The input language is as so:

    string number = integer
    fret action = short str
    fingerpos = <string number> <fret action>
    zeitpunkt = <fingerpos>(, <fingerpos>)*\n
    comment = # <...>\n

String number takes the convention that the first string is the low E string in
standard tuning.

And the input file/stream is just a series of zeitpunkten or comments.

What we have here is a relatively simple language serializing tablature. For
example, the E minor chord can be encoded as

    6 0, 5 2, 4 2, 3 0, 2 0, 1 0

You can also encode an arpeggio by

    6 0
    5 2
    4 2
    3 0
    2 0
    1 0
"""
from typing import List, Tuple
import re
import sys
import traceback

ZeitPunkten = Tuple[Tuple[Tuple[int, str], ...], ...]

def measured_chordstructor(zeitpunkten: ZeitPunkten, measure: int) -> str:
    start = 0
    tabs = [chordstructor(zeitpunkten[_s:_s + measure]) for _s in range(0, len(zeitpunkten), measure)]
    return "\n\n".join(tabs)

def chordstructor(zeitpunkten: ZeitPunkten) -> str:
    def note_width(fret_act: str) -> int:
        return len(fret_act) + 1

    lines: List[List[str]] = [['|'] for _ in range(6)]
    strings = set(range(6))

    for zp in zeitpunkten:
        zp_used = set()
        max_width_added = 0

        for fingerpos in zp:
            str_in = fingerpos[0] - 1
            zp_used.add(str_in)
            
            lines[str_in].append(str(fingerpos[1]))
            lines[str_in].append('-')
            max_width_added = max(max_width_added, note_width(fingerpos[1]))

        zp_blanks = strings - zp_used

        for blank in zp_blanks:
            lines[blank].append('-' * max_width_added)

    return "|\n".join(["".join(line) for line in lines])

def fixer(zeitpunkten: ZeitPunkten) -> str:
    translation = (6, 5, 4, 3, 2, 1)
    translated: List[str] = []

    for zp in zeitpunkten:
        timepoint = []
        for fingerpos in zp:
            new_fingerpos = (
                str(translation[fingerpos[0] - 1]),
                fingerpos[1]
            )
            timepoint.append(" ".join(new_fingerpos))

        translated.append(", ".join(timepoint))

    return "\n".join(translated)

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        zeitpunkten = []
        for linnum, line in enumerate(infile, 1):
            if line[0] == '#':
                continue
            try:
                line_parse = re.compile(",\s*").split(line)
                point: Tuple[Tuple[int, str], ...] = tuple((int(x.split()[0]), x.split()[1]) for x in line_parse)
                zeitpunkten.append(point)
            except IndexError:
                print("Syntax error at line %s: %s" % (linnum, line))
                print(traceback.format_exc())
                exit(1)

        print(measured_chordstructor(tuple(zeitpunkten), 30))
