import threading
from multiprocessing import Pool, Process, Queue, Lock
from concurrent.futures import ThreadPoolExecutor
import _thread
import time


# multi threads
# class MyThread(threading.Thread):
#     def __init__(self, thread_name, thread_id):
#         super(MyThread, self).__init__()
#         # threading.Thread.__init__(self)
#         self.name = thread_name
#         self.id = thread_id
#
#     def run(self) -> None:
#         print("Thread {}, {} start".format(self.name, self.id))
#         time.sleep(2)
#         print(time.time())
#         print("Thread {}, {} end".format(self.name, self.id))


# threads = []
# for i in range(2):
#     threads.append(MyThread("thread" + str(i + 1), i + 1))
#
# for i in range(len(threads)):
#     threads[i].start()
#
# for i in range(len(threads)):
#     threads[i].join()
#
# print("main thread finished")



# multi process
# class MyProcess(Process):
#     def __init__(self, process_name):
#         super(MyProcess, self).__init__()
#         self.name = process_name
#     def run(self):
#         print("Process {} start".format(self.name))
#         time.sleep(2)
#         print(time.time())
#         print("Process {} end".format(self.name))
#
# if __name__ == "__main__":
#     process_list = []
#     for i in range(3):
#         process_list.append(MyProcess("process" + str(i + 1)))
#
#     for i in range(len(process_list)):
#         process_list[i].start()
#
#     for i in range(len(process_list)):
#         process_list[i].join()
#
#     print("Main process finished")

def process_task(process_num):
    print("Process {} start".format(process_num))
    time.sleep(2)
    print(time.time())
    print("Process {} end".format(process_num))
#
#
# if __name__ == "__main__":
#     process_list = []
#     for i in range(3):
#         process_list.append(Process(target=process_task, args=("process" + str(i + 1),)))
#
#     for i in range(len(process_list)):
#         process_list[i].start()
#
#     for i in range(len(process_list)):
#         process_list[i].join()
#
#     print("Main process finished")

# Process Pool

# if __name__ == "__main__":
#     process_pool = Pool(5)
#     for i in range(10):
#         process_pool.apply_async(process_task, args=("process" + str(i + 1), ))
#
#     process_pool.close()
#     process_pool.join()
#     print("Main process finished")

if __name__ == "__main__":
    thread_pool = ThreadPoolExecutor()