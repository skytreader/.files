#!/usr/bin/env python3
from argparse import ArgumentParser
from datetime import datetime, timedelta

import re
import sys

def make_srt_timestamp(dt):
    return ("%02d:%02d:%02d,%03d" % (dt.hour, dt.minute, dt.second, dt.microsecond))

def fix_microsecond(dt):
    return datetime(
        year=dt.year, month=dt.month, day=dt.day, hour=dt.hour,
        minute=dt.minute, second=dt.second,
        microsecond=int(dt.microsecond / 1000)
    )

if __name__ == "__main__":
    parser = ArgumentParser(description="adjust offset of timestamps in srt files")
    parser.add_argument(
        "--srt", "-s", required=True, type=str,
        help="The path to the SRT file to adjust."
    )
    parser.add_argument(
        "--output", "-o", required=False, type=str,
        help="The path to which we output the adjusted SRT file. If not specified, print to stdout."
    )
    parser.add_argument(
        "--delta", "-d", required=True, type=int,
        help="The offset adjustment in seconds. Can be negative."
    )
    args = vars(parser.parse_args())
    # Not so clean coding. But this is just a one-off script.
    outfile = open(args["output"], "w+") if args.get("output") is not None else sys.stdout
    timeframe_re = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")
    adjustment_delta = timedelta(seconds=args["delta"])
    
    with open(args["srt"]) as srt_file:
        for line in srt_file:
            if timeframe_re.match(line):
                start, end = line.split(" --> ")
                start_ts = fix_microsecond(datetime.strptime(start.strip(), "%H:%M:%S,%f"))
                end_ts = fix_microsecond(datetime.strptime(end.strip(), "%H:%M:%S,%f"))
                adj_start_ts = start_ts + adjustment_delta
                adj_end_ts = end_ts + adjustment_delta
                print(
                    "%s --> %s" %
                    (
                        make_srt_timestamp(adj_start_ts), make_srt_timestamp(adj_end_ts)
                    ),
                    file=outfile
                )
            else:
                print(line, file=outfile, end="")

    if args["output"] is not None:
        outfile.close()
