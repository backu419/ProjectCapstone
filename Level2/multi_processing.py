import multiprocessing as mp
from Level1 import level1 as l1, demo as d
from time import perf_counter


def dri():
    l1.drives_info()


def search_file(drii, inp):
    dr = drii
    np = inp
    d.drive_search(dr, np)


# start = perf_counter()
# print("Number of processors: ", mp.cpu_count())
# ri = input("Enter drive name in formate of C:\\ or D:\\ : ")
# ip = input("What are you searching for? :> ")
# dri()
# search_file(ri, ip)
# end = perf_counter()
# print(f'time taken to perform : {end - start} seconds')
# print("hi")

if __name__ == '__main__':
    start = perf_counter()
    print("Number of processors: ", mp.cpu_count())
    ri = input("Enter drive name in formate of C:\\ or D:\\ : ")
    ip = input("What are you searching for? :> ")
    p1 = mp.Process(target=dri)
    p2 = mp.Process(target=search_file, args=(ri, ip))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = perf_counter()
    print(f'time taken to perform : {end - start} seconds')
