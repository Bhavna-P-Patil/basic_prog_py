



# Iteration approach
def StartDynamic(No,Message):
    iCnt =0
    while iCnt<No:
        print("Message")
        iCnt = iCnt + 1


    

def main():
    print("Enter number of times you want to display message on screen")
    value=int(input())
    print("Enter the message")
    name =input()

    StartDynamic(value,name)
    StartDynamic(value)

if __name__=="__main__":
    main()
