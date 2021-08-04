# Accept N numbers from user and filterout only even numbers from that N numbers.
#After that add 2 in every even number.
# after the addition of 2 perform summation of that modified number.
# Input[1,3,2,4,6,5,4]
# after filter[2,4,4]
# after map[4,6,6]
# after reduce[16]
def CheckEven(no):
    if no% 2==0:
        return True
    else:
        return False


def marvellousFilter(arr):
    brr =[]
    for i in range(len(arr)):
        if CheckEven(arr[i])==True:
            brr.append(arr[i])
    return brr


def marvellousMap(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]+2
    return arr


def marvellousReduce(brr):
    sum=0
    for i in range(len(brr)):
        sum = sum+brr[i]
    return sum

def main():
    arr =[]
    print("enter number of elements")
    size= int(input())
    

    for i in range(size):
        print("enter element number:",i+1)
        no = int(input())
        arr.append(no)

    print("your enter data is:",arr)

    newdata = marvellousFilter(arr)
    print("after filtering data is:",newdata)

    newdata1 = marvellousMap(newdata)
    print("after maping data is:",newdata1)

    output= marvellousReduce(newdata1)
    print("after reduce data is:",output)

if __name__=="__main__":
    main()
