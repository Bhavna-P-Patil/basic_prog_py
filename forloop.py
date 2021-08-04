




def DisplayF(value):
    print("Output of for loop")
    iCnt = 0
    for iCnt in range(0,value):
        print("jay Ganesh")


def DisplayW(value):
    print("Output of while loop")
    iCnt = 0
    while iCnt < value:
        print("jay Ganesh")
        iCnt = iCnt+1


def main():
    print("Enter the number of iteration")
    no = int(input())

    DisplayF(no)
    DisplayW(no)




if __name__=="__main__":
    main()
