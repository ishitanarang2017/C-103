import sys, time, random, os, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source = "C:/Users/Ishita Narang/Downloads"

class Fileremover(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path+" has been created")
    def on_deleted(self, event):
        print(event.src_path+" has been deleted")
    def on_modified(self, event):
        print(event.src_path+" has been modified")
    def on_moved(self, event):
        print(event.src_path+" has been moved")
        

Eventhandler = Fileremover()
observer = Observer()
observer.schedule(Eventhandler,source,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("till running")
except KeyboardInterrupt:
    print("stopping...")
    observer.stop()