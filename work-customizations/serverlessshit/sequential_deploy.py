#!/usr/bin/env python3
from argparse import ArgumentParser
from pprint import pprint

import subprocess
import yaml

def construct_arg(k, v):
    if len(k) == 1:
        return "-%s %s" % (k, v)
    else:
        return "--%s=%s" % (k, v)

def compose_args(args):
    # TODO Do not accept function because that's our thing
    return " ".join([construct_arg(k, v) for k, v in args.items() if (
        v != "" and v is not None and (k != "f" or k != "function"
    ))])

if __name__ == "__main__":
    # Using this because we might want to expand arguments in the future
    # Should be 1:1 parity with serverless deploy args.
    parser = ArgumentParser(description="sequentially deploy sls functions")
    parser.add_argument(
        "--stage", "-s", type=str, help="deployment stage"
    )
    args = compose_args(vars(parser.parse_args()))

    with open("serverless.yml") as slsyml:
        functions = yaml.safe_load(slsyml).get("functions", {})

        for fn in functions.keys():
            cmd_string = "sls deploy %s --function=%s" % (args, fn)
            print("deploying %s" % fn)
            print(cmd_string)
            subprocess.run(cmd_string, shell=True)
