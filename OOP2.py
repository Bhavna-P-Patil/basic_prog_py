

def Add(no1,no2):
    return no1+no2
    
    
def Sub(no1,no2):
    return no1-no2        



def main():
    print("enter 1st number")
    value1=int(input())
    print("enter 2nd number")
    value2=int(input())
    
    ret= Add(value1,value2)
    print("addition is:",ret)
    
    ret = Sub(value1,value2)
    print("substraction is:",ret)




if __name__=="__main__":
    main()