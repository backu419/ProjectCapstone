import multiprocessing as mp
from Level1 import level1 as l1, demo as d
from time import perf_counter
from threading import Thread
def drives():
    l1.drives_info()
def searchfile():
    d.drive_search(dr, inp)
start_time = perf_counter()
dr = input("Enter drive name in formate of C:\\ or D:\\ : ")
inp = input("What are you searching for? :> ")
t1 = Thread(target=drives)
t2 = Thread(target=searchfile)
t1.start()
t2.start()
t1.join()
t2.join()
print("Number of processors: ", mp.cpu_count())
end_time = perf_counter()
print(f'Time taken to perform : {end_time - start_time} seconds')