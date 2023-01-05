from time import perf_counter
import os, multiprocessing as mp


class searchfile:
    def __init__(self):
        pass

    def task2(self, drive, s):
        try:
            c = 0
            for root, dirs, files in os.walk(drive):
                for name in files:
                    filepath = os.path.join(root, name)
                    if s in name:
                        c = c+1
                        print(filepath)
            if c == 0:
                print("file not found")
            else:
                print(f"{c} files")

        except:
            print("no error")

    def run(self):
        pass


if __name__ == '__main__':
    ri, ip= input("Enter drive name in formate of C:\\ or D:\\ : "), input("What are you searching for? :> ")
    start = perf_counter()
    p1 = mp.Process(target=searchfile.run, args=(ri, ip))
    p1.start()
    p1.join()
    end = perf_counter()
    print(f'time taken to perform : {end - start} seconds')
