# Inbuilt function from module

def Substraction(no1,no2):         # 100
    return no1-no2

def SubDecorator(func_name):      # 200   func_name=100
    def Updator(a,b):             # 300
        if a<b:              # first parameter is small
            a,b=b,a
        return func_name(a,b)        # return (call 100(10,6))  ->4

    return Updator             # return300


def main():                        # 400
    Sub=SubDecorator(Substraction)   # cll200(100)   sub contains 300

    print("Enter 1st no")
    value1=int(input())      # 6
    print("Enter 2nd no")    # 10
    value2=int(input())


    ret = Sub(value1,value2)      # call 300(6,10)
    print("substraction is",ret)        # substraction is 4



if __name__=="__main__":
    main()                          # call 400