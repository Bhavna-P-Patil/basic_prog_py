# Inbuilt function from module

def Substraction(no1,no2):
    print("4: Inside Substraction")
    return no1-no2

def SubDecorator(func_name):
    print("7:Inside SubDecorator")
    def Updator(a,b):
        if a<b:              # first parameter is small
            a,b=b,a
        return func_name(a,b)

    return Updator


def main():
    print("16:Inside main")
    Sub=SubDecorator(Substraction)

    print("Enter 1st no")
    value1=int(input())
    print("Enter 2nd no")
    value2=int(input())


    ret = Sub(value1,value2)
    print("substraction is",ret)
    print("26: End of main")


if __name__=="__main__":
    print("30: Inside starter")
    main()