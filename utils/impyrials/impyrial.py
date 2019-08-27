from argparse import ArgumentParser
from abc import ABC, abstractmethod
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import logging
import os
import shutil
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class CopyFileHandler(FileSystemEventHandler):

    def __init__(self, copyto, is_dir=False):
        super().__init__()

        if os.path.exists(copyto):
            if os.path.isdir(copyto) != is_dir:
                if is_dir:
                    raise NotADirectoryError(
                        "Handler was set-up to handle directories but %s is not a directory." % copyto
                    )
                else:
                    raise IsADirectoryError(
                        "Handler was set-up to handle files but %s is a directory." % copyto
                    )
            else:
                self.copyto = copyto
                self.is_dir = is_dir
        else:
            raise FileNotFoundError("Specified copyto location not found: %s" % copyto)

    def __is_jar_event(self, event):
        return not event.is_directory and event.src_path.endswith(".jar")

    def on_created(self, event):
        super().on_created(event)
        if self.__is_jar_event(event):
            logging.info("JAR created: %s" % event.src_path)
            shutil.copy(event.src_path, self.copyto)

    def on_modified(self, event):
        super().on_modified(event)
        if self.__is_jar_event(event):
            logging.info("JAR modified: %s" % event.src_path)
            shutil.copy(event.src_path, self.copyto)

class Impyrial(object):

    def __init__(self, watch, event_handler):
        self.watch = watch
        self.event_handler = event_handler

    def guard(self):
        observer = Observer()
        observer.schedule(
            self.event_handler,
            self.watch,
            recursive=False
        )
        observer.start()
        logging.info("Now watching %s" % self.watch)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

if __name__ == "__main__":
    impyrial = Impyrial(
        os.environ["IMPYRIAL_SOURCE"],
        CopyFileHandler(os.environ["IMPYRIAL_TARGET"], True)
    )
    impyrial.guard()
