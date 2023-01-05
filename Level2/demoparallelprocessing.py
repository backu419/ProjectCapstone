import multiprocessing as mp
from time import perf_counter
import math
result1=[]
result2=[]
def cal_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
def cal_twe(number):
    for i in number:
        result2.append(math.sqrt(i**5))

numlist=list(range(1200000))
start=perf_counter()
cal_one(numlist)
cal_twe(numlist)
end=perf_counter()
print(f'time taken to perform : {end - start} seconds')
print("hi")
if __name__=='__main__':
    numlist=list(range(2500000))
    p1=mp.Process(target=cal_one, args=(numlist,))
    p2=mp.Process(target=cal_twe, args=(numlist,))
    start=perf_counter()
    # cal_one(numlist)
    # cal_twe(numlist)
    p1.start()
    p2.start()
    end=perf_counter()
    print(f'time taken to perform : {end-start} seconds')
    # print(result1)
    # print(result2)
