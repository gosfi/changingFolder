from watchdog.events import FileSystemEventHandler

import json
import os
import time


class MyHandler(FileSystemEventHandler):
    def change_folder(self):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            if filename.endswith(".pdf") or filename.endswith(".epub"):
                folder_destination = "C:\\Users\\Samuel\\Desktop\\books"
            elif filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
                folder_destination = "C:\\Users\\Samuel\\Desktop\\images"
            else:
                folder_destination = folder_to_track
            new_destination = folder_destination + "\\" + filename
            os.rename(src, new_destination)


folder_to_track = "C:\\Users\\Samuel\\Downloads"
folder_destination = ""
handler = MyHandler()
handler.change_folder()
