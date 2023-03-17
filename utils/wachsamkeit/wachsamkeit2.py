import json
import logging
import os
import random
import requests
import sys
import time

from notifypy import Notify

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specify user to watch...")

    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Watching user %s" % sys.argv[1])
    snapshot_filename = "%s-snapshot.json" % sys.argv[1]
    snapshot = {}
    
    if not os.path.isfile("snapshot.json"):
        initial = requests.get("https://hacker-news.firebaseio.com/v0/user/%s.json" % sys.argv[1])
        with open(snapshot_filename, "w") as snapjson:
            snapjson.write(initial.text)

    with open(snapshot_filename) as snapjson:
        snapshot = json.load(snapjson)

    try:
        while True:
            r = requests.get("https://hacker-news.firebaseio.com/v0/user/%s.json" % sys.argv[1])
            if r.status_code == 200:
                data = json.loads(r.text)
                if len(snapshot["submitted"]) < len(data["submitted"]):
                    logging.info("Activity detected!")
                    with open(snapshot_filename, "w") as snapjson:
                        snapjson.write(r.text)
                    msg = Notify()
                    msg.title = "WATCH OUT!"
                    msg.message = "Updated!"
                    msg.send()
                else:
                    logging.info("Checked but no dice.")
            
            time.sleep(random.randrange(1, 600))
    except KeyboardInterrupt:
        exit(1)
