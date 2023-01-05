import os
from time import perf_counter


def location_search(filename, path):
    for r, d, f in os.walk(path):
        for file in f:
            if file == filename:
                print("File you searched for " + filename + " is available")
                break
        else:
            print("File you searched for " + filename + " is not available")


start_time = perf_counter()
na = input("enter the file name for searching: ")
pa = input("Enter the path: ")
location_search(na, pa)
end_time = perf_counter()
print(f'Time taken to perform : {end_time-start_time} seconds')
