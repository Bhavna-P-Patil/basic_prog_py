

import moduleSlection1 as mS
# import moduleSlection *


def main():
    print("Enter one number")
    value= int(input())

    bret = mS.CheckEven(value)

    if bret == True:
        print("{}is even number".format(value))
    else:
        print("{} is odd number".format(value))


    


if __name__=="__main__":
    main()
