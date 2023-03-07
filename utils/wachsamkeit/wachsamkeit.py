import logging
import random
import requests
import time

from notifypy import Notify

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Watching Rijksmuseum for tickets...")
    try:
        while True:
            r = requests.get("https://www.rijksmuseum.nl/en/tickets")
            if r.status_code == 200:
                if "Try again later" not in r.text:
                    msg = Notify()
                    msg.title = "WATCH OUT!"
                    msg.message = "Maybe tickets are available now"
                    msg.send()
                else:
                    logging.info("Checked but no dice.")
            
            time.sleep(random.randrange(1, 40))
    except KeyboardInterrupt:
        exit(1)
