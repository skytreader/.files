"""
Construct guitar TABlature from an input language. The input language is as so:

    string number = integer
    fret action = short string
    fingerpos = <string number> <fret action>
    zeitpunkt = <fingerpos>(, <fingerpos>)*\n

String number takes the convention that the first string is the low E string in
standard tuning.

And the input file/stream is just a series of zeitpunkten.
"""
from typing import List, Tuple
import re
import sys

ZeitPunkten = Tuple[Tuple[Tuple[int, str], ...], ...]

def measured_chordstructor(zeitpunkten: ZeitPunkten, measure: int) -> str:
    start = 0
    tabs = [chordstructor(zeitpunkten[_s:_s + measure]) for _s in range(0, len(zeitpunkten), measure)]
    return "\n".join(tabs)

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

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        zeitpunkten = []
        for line in infile:
            line_parse = re.compile(",\s*").split(line)
            point: Tuple[Tuple[int, str], ...] = tuple((int(x.split()[0]), x.split()[1]) for x in line_parse)
            zeitpunkten.append(point)

        print(measured_chordstructor(tuple(zeitpunkten), 30))
