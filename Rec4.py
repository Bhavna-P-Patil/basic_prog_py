
def AdditionF(data):
    sum=0
    for i in range(len(data)):sum = sum+data[i]
    return sum

def AdditionW(data):
    sum=0
    while i< len(data):
        sum=sum+data[i]
        i=i+1
    return sum



sum=0
i=0
def AdditionR(data):         # recursive logic
    global sum
    global i
    if i <len(data):
        sum=sum+data[i]
        i=i+1
        Addition(data)
    return sum


def main():
    arr=[]
    size=int(input("Enter the size of array"))
    for i in range(size):arr.append(int(input()))

        
    print("data is",arr)

    print("addition is ",AdditionF(arr))

    print("addition is ",AdditionW(arr))

    print("recursion data is",AdditionR(arr))

if __name__ =="__main__":
    main()
