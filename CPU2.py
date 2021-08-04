# Parellel Processing

import os
import multiprocessing
import time
def Square(no):
    return no*no
#####################################################

def ParallelProcessing():
    start = time.time()
    print("Parallel processing")
    arr =range(100)


    pobj = multiprocessing.Pool()

    ret = pobj.map(Square,arr)

    end=time.time()
    print("Time required for parallel execution",end-start)

############################################################
def SerialProcessing():
    start = time.time()
    print("Serial processing")
    arr=range(100)
    ret = []

    for i in arr:
        ret.append(Square(i))

    #print("Result of serial processing os",ret)
    end = time.time()
    print("Time required for serial execution",end-start)
################################################################
def main():
    print("Inside main")
    ParallelProcessing()
    SerialProcessing()

if __name__=="__main__":
    main()