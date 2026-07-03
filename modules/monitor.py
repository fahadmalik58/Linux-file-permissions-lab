from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler

import time


class Monitor(

    FileSystemEventHandler

):

    def on_modified(

            self,

            event

    ):

        print(

            "Modified:",

            event.src_path

        )


def watch(path):

    observer = Observer()

    observer.schedule(

        Monitor(),

        path,

        recursive=True

    )

    observer.start()

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()