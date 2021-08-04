# with synchronization
import threading

Amount = 1000
def ATM(func,kulup):
    func(kulup)

def Deposit(kulup):
    kulup.acquire()
    value= int(input("Enter the amount to deposit"))
    global Amount
    Amount =Amount + value
    print("Deposite successful - Balance :",Amount)
    kulup.release()

def Withdraw(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to withdraw"))
    global Amount
    if value> Amount:
        print("There is no sufficient balance")
    else:
        Amount = Amount-value
        print("Withdraw succesful - Balance:",Amount)
    kulup.release()

def main():
    print("Inside main")

    kulup = threading.Lock()
    t1 = threading.Thread(target =ATM,args =(Deposite,kulup,))
    t2 = threading.Thread(target =ATM,args =(Withdraw,kulup))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("ATM application closed")




if __name__=="__main__":
    main()