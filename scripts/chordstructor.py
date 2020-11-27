"""
Construct guitar TABlature from an input language. The input language is as so:

    fingerpos = <string number> <fret>
    zeitpunkt = <fingerpos>(, <fingerpos>)*\n

String number takes the convention that the first string is the low E string in
standard tuning.

And the input file/stream is just a series of zeitpunkten.
"""
from typing import List, Tuple
import sys

ZeitPunkten = Tuple[Tuple[Tuple[int, int], ...], ...]

def measured_chordstructor(zeitpunkten: ZeitPunkten, measure: int) -> str:
    start = 0
    tabs = [chordstructor(zeitpunkten[_s:_s + measure]) for _s in range(0, len(zeitpunkten), measure)]
    return "\n".join(tabs)

def chordstructor(zeitpunkten: ZeitPunkten) -> str:
    def note_width(fret_no: int) -> int:
        return 3 if fret_no >= 10 else 2

    lines: List[List[str]] = [['|'] for _ in range(6)]
    strings = set(range(6))

    for zp in zeitpunkten:
        zp_used = set()
        max_width_added = 0

        for fingerpos in zp:
            str_in = fingerpos[0] - 1;
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
            point = [int(x) for x in line]
            if len(point) % 2:
                print("'%s' should contain an even count of numbers" % line)
                exit(1)
            string_nums = point[::2]
            fret_nums = point[1::2]
            zeitpunkten.append(tuple(zip(string_nums, fret_nums)))

        print(measured_chordstructor(tuple(zeitpunkten), 30))
