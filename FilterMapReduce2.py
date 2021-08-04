# Accept N numbers from user and filterout only even numbers from that N numbers.
#After that add 2 in every even number.
# after the addition of 2 perform summation of that modified number.


# Input[1,3,2,4,6,5,4]

# after filter[2,4,4]
# after map[4,6,6]
# after reduce[16]

import functools

 CheckEven= lambda no:(no%2==0)
 Increment= lambda no:no+2
 Add =lambda no1,no2:no1+no2

def Increment(no):
    return no+2


def Add(no1,no2):
    return no1+no2


def main():
    arr =[]
    print("enter number of elements")
    size= int(input())
    
            
    

    for i in range(size):
        print("enter element number:",i+1)
        no = int(input())
        arr.append(no)


    print("your enter data is:",arr)
    #newdata = filter(function_name,data)
    newdata=list(filter(CheckEven,arr))        #newdata = marvellousFilter(arr)
    print("after filtering data is:",newdata)

    newdata1= list(map(Increment,newdata))     #newdata1 = marvellousMap(newdata)
    print("after maping data is:",newdata1)    #print("after maping data is:",newdata1)


    output= functools.Reduce(Add,newdata1)               #output= marvellousReduce(newdata1)
    print("after reduce data is:",output)     #print("after reduce data is:",output)

    
                            




if __name__=="__main__":
    main()
