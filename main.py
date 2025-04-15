import os
import random
import time

import dotenv

from checkers.velostrana import VelostranaChecker
from checkers.velosklad import VeloskladChecker
from notifier import Notifier


def run() -> None:
    dotenv.load_dotenv()

    token = os.getenv("TOKEN")
    chant_id = os.getenv("CHAT_ID")
    if token is None or chant_id is None:
        raise Exception("TOKEN or CHAT_ID environment variable not set")

    notifier = Notifier(token, chant_id)

    checkers = {
        "Велострана": VelostranaChecker(),
        "Велосклад": VeloskladChecker()
    }
    notifier.send_message("Start working parser")
    try:
        while True:
            time.sleep(random.randrange(start=5, stop=20))
            for name, checker in checkers.items():

                avail = checker.check_availability()
                if avail:
                    notifier.send_message(f"ASPECT COVENANT доступен в {name}!!!")

    except Exception as e:
        notifier.send_message("Error while parsing: {0}".format(str(e)))




if __name__ == "__main__":
    run()