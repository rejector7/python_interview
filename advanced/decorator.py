import time
from functools import wraps


def run_time(func):
    @wraps(func)
    def normal_add_run_time(name):
        time1 = time.time()
        func(name)
        time2 = time.time()
        t = time2 - time1
        return print("My name is {0}, run for {1} seconds".format(name, t))
    return normal_add_run_time


@run_time
def normal_func(name):
    time.sleep(5)
    # print("My name is {0}.".format(name))


# normal_func("rjt")
# print(normal_func.__name__)



# @ property

