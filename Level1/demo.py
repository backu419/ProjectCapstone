import os  # from time import perf_counter


def drive_search(drive, Input):
    counter = 0
    for r, d, f in os.walk(drive):  # if need we can change the hard drive as per need
        for file in f:
            filepath = os.path.join(r, file)
            if Input in file:
                counter += 1
                print(filepath)
    if counter == 0:
        print("No file found.")
    else:
        print(f" {counter} files found.")
# start_time = perf_counter()
# dr = input("Enter drive name in formate of C:\\ or D:\\ : ")
# drive_search(dr)
# end_time = perf_counter()
# print(f'Time taken to perform : {end_time-start_time} seconds')
