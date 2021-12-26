#!/usr/bin/env python3

import json
import os
import re
import subprocess
import sys

cli_input_form = re.compile(r"\{\d+\}")

def mount_substitute(source, target, cli_inputs):
    template = "--mount type=bind,source='%s',target='%s'"
    if cli_input_form.match(target):
        try:
            return template % (source, target.format(*cli_inputs))
        except IndexError:
            raise Exception("Not enough CLI inputs provided.")
    else:
        return template % (source, target)

def compose_mounts(cwd, mounts, cli_inputs):
    # FIXME There's a myriad of ways `source` might be specified. I specify it
    # relative but it should also work if it is specified as an absolute path.
    mounts_composed = [
        mount_substitute(os.path.join(cwd, source), target, cli_inputs)
        for source, target in mounts.items()
    ]
    return " ".join(mounts_composed)

def compose_env_string(envs):
    # FIXME Not sure how this will behave under extensive quoting.
    envvars = ["%s=%s" % (k, v) for k, v in envs.items()]
    compose_param_str = zip(["-e" for x in range(len(envvars))], envvars)
    return " ".join("%s %s" % x for x in compose_param_str)

if __name__ == "__main__":
    # This filename is reserved
    docker_rennen_file = "docker-rennen.json"

    # read config
    with open(docker_rennen_file) as json_config:
        config = json.load(json_config)
        docker_image = config["image"]
        mounts = config.get("mounts", {})
        envs = compose_env_string(config.get("env", {}))

        command = "docker run %s %s %s" % (
            compose_mounts(os.getcwd(), mounts, sys.argv[1:]),
            envs,
            docker_image
        )
        print(command)
        #subprocess.run(command, shell=True)
