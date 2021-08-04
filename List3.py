def Addition(LIST):
    sum = 0
    for i in range(len(LIST)):
        sum = sum + LIST[i]
    return sum   
    

def main():
    Arr = []
    print("Enter the number of elements")
    size= int(input())


    print("Enter the elements")
    for i in range(size):
        print("Enter the element no:",i+1)
        value = int(input())
        Arr.append(value)

    print("Accepted data is:",Arr)

    ret = Addition(Arr)


    print("Addition of all elements is:",ret)

if __name__=="__main__":
    main()



 #indexed
# sequential
# heterogenious
# mutable
