import threading
from multiprocessing import Pool
from concurrent.futures import thread
import time


class MyThread(threading.Thread):
    def __init__(self, thread_name, thread_id):
        threading.Thread.__init__(self)
        self.name = thread_name
        self.id = thread_id

    def run(self) -> None:
        print("Thread {}, {} start".format(self.name, self.id))
        time.sleep(2)
        print(time.time())
        print("Thread {}, {} end".format(self.name, self.id))


threads = []
for i in range(2):
    threads.append(MyThread("thread" + str(i + 1), i + 1))

for i in range(len(threads)):
    threads[i].start()

for i in range(len(threads)):
    threads[i].join()


