import os
from time import perf_counter
from threading import Thread


def task():
    print()


start_time = perf_counter()
t1 = Thread(target=task)
t2 = Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = perf_counter()
print(f'Time taken to perform : {end_time-start_time} seconds')