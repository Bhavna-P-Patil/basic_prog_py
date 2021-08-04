# Serial processing

import os
import time
def Square(no):
    return no*no

def SerialProcessing():
    start = time.time()
    print("Serial processing")
    arr=range(10)
    ret = []

    for i in arr:
        ret.append(Square(i))

    #print("Result of serial processing os",ret)
    end = time.time()
    print("Time required for serial execution",end-start)

def main():
    print("Inside main")
    SerialProcessing()


if __name__=="__main__":
    main()