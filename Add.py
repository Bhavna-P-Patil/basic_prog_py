def Addition(Arr):
    sum=0

    for no in Arr:
        sum=sum+no
        return sum

def main():    
    ret = Addition(10,20)
    print("Addition is:",ret)

    ret = Addition(12,52)
    print("Addition is:",ret)

if __name__=="__main__":
    main()
