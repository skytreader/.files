#!/usr/bin/python3

# /// script
# requires-python = ">=3.8"
# dependencies = ["python-ffmpeg"]
# ///

from argparse import ArgumentParser
from ffmpeg import FFmpeg

if __name__ == "__main__":
    parser = ArgumentParser(description="extract a bunch of screenshots from a video file")
    parser.add_argument(
        "--input", "-i", required=True, type=str,
        help="The video file to extract screenshots from."
    )
    timestamps_arg_group = parser.add_mutually_exclusive_group(required=True)
    timestamps_arg_group.add_argument(
        "--timestamps-file", "-f", type=str,
        help="A text file listing the timestamps to be extracted. Put one timestamp per line."
    )
    timestamps_arg_group.add_argument(
        "--timestamps-list", "-l", type=str,
        help="Comma-separated timestamps to be extracted."
    )
    parser.add_argument(
        "--output", "-o", required=True, type=str,
        help="Directory path to save screenshots to."
    )
