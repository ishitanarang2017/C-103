import sys, time, random, os, shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source = "C:/Users/Ishita Narang/Downloads"
dest = "C:/Users/Ishita Narang/Desktop/backup"
dirtree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
class Fileremover(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dirtree.items():
            time.sleep(1)
            if extension in value:
                filename = os.path.basename(event.src_path)
                print("downloaded "+ filename)
                path1 = source+'/'+filename
                path2 = dest +'/'+key
                path3= dest+'/'+key+ '/'+ filename
                if os.path.exists(path2):
                    print("moving to existing directory")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    print("creating directory and moving files")
                    time.sleep(1)

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