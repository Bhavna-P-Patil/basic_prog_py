

def Addition(no1,no2,no3):
    return no1+no2+no3

def main():
    print("Enter first number")
    value1= int(input())

    print("Enter 2nd number")
    value2= int(input())

    print("Enter third nu")
    value3= float(input())

    ret= Addition(value1,value2,value3)

    print("Addition is",ret)


if __name__=="__main__":
    main()
