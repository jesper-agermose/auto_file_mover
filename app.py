import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from configparser import ConfigParser

#Auto moves files from one directory and into another.
#Set the origin directory and destination and run the script.

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    org = config.get('config', 'org')
    dest = config.get('config', 'dest')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, org, recursive=True)
    observer.start()    
    count = True

    try:
        
        while True:
            time.sleep(10)
            print("Checking files...")
            files = os.listdir(org)   
            if len(files) > 0:                     
                for file in files:
                    shutil.move((org + file), dest)
                    print(file + " moved.")
            else:
                print("No files to move.")          
    finally:        
        observer.stop()
        observer.join()