# Inbuilt function from module

def Substraction(no1,no2):
    return no1-no2

def SubDecorator(func_name):
    def Updator(a,b):
        if a<b:              # first parameter is small
            a,b=b,a
        return func_name(a,b)

    return Updator


def main():
    Sub=SubDecorator(Substraction)

    print("Enter 1st no")
    value1=int(input())
    print("Enter 2nd no")
    value2=int(input())


    ret = Sub(value1,value2)
    print("substraction is",ret)



if __name__=="__main__":
    main()