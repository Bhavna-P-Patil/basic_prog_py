import os
import threading
from time import sleep
def Thread1(no):
    print(" thread1 is created")
    print("PID of thread1 is:",os.getpid())
    print("PID of parent thread1 is",os.getppid())
    for i in range(no):
        sleep(1)
        print("Thread-1",i)

def Thread2(no):
    print(" thread2 is created")
    print("PID of thread2 is:", os.getpid())
    print("PID of parent thread2 is", os.getppid())
    for i in range(no):
        sleep(1)
        print("thread-2",i)

def main():
    print("Inside main thread")
    print("PID of current process is",os.getpid())
    print("PID of parent process is",os.getppid())
    value=10
    t1=threading.Thread(target=Thread1,args=(value,))
    t2=threading.Thread(target=Thread2,args=(value,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


    print("End of main process")

if __name__=="__main__":
    main()