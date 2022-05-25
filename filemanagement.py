import shutil
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import splitext, exists
from os import scandir, rename
from shutil import move
from time import sleep

source_dir = "C:\\Users\\Magic\\Downloads"
dest_dir_pdf= "C:\\Users\\Magic\\Downloads\\DownloadedPDFs"
dir_list = os.listdir(source_dir)

def makeUnique(path):
    filename, extension = splitext(path)
    counter = 1
    while exists(path):
        path = f"{filename} ({counter}){extension}"
        counter = counter + 1

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "\\" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)







class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for entry in dir_list:
            name = entry
            dest = source_dir
            if name.endswith(".pdf"):
                dest = dest_dir_pdf
                move(dest, entry, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



# path = "C://Users//Magic//Downloads"

# dir_list = os.listdir(path)

# for item in dir_list:
#     print(item)