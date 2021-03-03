#!/usr/bin/env python3

import json
import os
import subprocess

def compose_mounts(cwd, mounts):
    template = "--mount type=bind,source='%s',target='%s'"
    mounts_composed = [
        template % (os.path.join(cwd, source), target)
        for source, target in mounts.items()
    ]
    return " ".join(mounts_composed)

if __name__ == "__main__":
    # read config
    with open("docker-rennen.json") as json_config:
        config = json.load(json_config)
        docker_image = config["image"]
        mounts = config["mounts"]

        print("docker run %s %s" % (compose_mounts(os.getcwd(), mounts), docker_image))
