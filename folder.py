from watchdog.events import FileSystemEventHandler

import json
import os
import time


class MyHandler(FileSystemEventHandler):
    def change_folder(self):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            #insert as much file type as you want here
            if filename.endswith(".pdf") or filename.endswith(".epub"):
                folder_destination = ""
            elif filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"):
                folder_destination = ""
            else:
                #if none of the types work, don't move this file
                folder_destination = folder_to_track
            new_destination = folder_destination + "\\" + filename
            os.rename(src, new_destination)

#insert which folder to look at
folder_to_track = ""
folder_destination = ""
handler = MyHandler()
handler.change_folder()
