import os, sys, time

from fnmatch import fnmatch
from Queue import Queue

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

if sys.platform.startswith('darwin'): from notify import notify_on_darwin as notify
elif sys.platform.startswith('win32'): from notify import notify_on_windows as notify
elif sys.platform.startswith('linux'): from notify import notify_on_linux as notify


class EventHandler(FileSystemEventHandler):
    def __init__(self, queue):
        self.queue = queue
        self.ignore = ['.*','~*','*.bac']

    def on_any_event(self, event):
        head, tail = os.path.split(event.src_path) 
        match = [fnmatch(tail, p) for p in self.ignore]
        if True not in match:
            self.queue.put(tail)


class WatchMan():
    def __init__(self, name, path):
        self.name = name
        self.path = path
       
        self.queue = Queue()
        event_handler = EventHandler(self.queue)
       
        self.observer = Observer()
        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

    def get_changes(self):
        files = []
        for i in range(self.queue.qsize()):
            item = self.queue.get() 
            if item not in files:
                files.append(item)  
            self.queue.task_done()
        
        return files

    def start(self):
        notify('Starting GitBox','...')
        qsize = self.queue.qsize()
        lastchange = time.time()
        while True:
            if qsize != self.queue.qsize():
                lastchange = time.time()

            if time.time()-lastchange >= 10 and self.queue.qsize() > 0:
                files = self.get_changes()
                notify('GitBox Sync for:', ', '.join(files))
            
            qsize = self.queue.qsize()
            time.sleep(1)


    def stop(self):
        self.observer.stop()
        self.observer.join()

if  __name__ == "__main__":

    wm = WatchMan('Document' , sys.argv[1])

    try:
        wm.start()
    except KeyboardInterrupt:
        wm.stop()
