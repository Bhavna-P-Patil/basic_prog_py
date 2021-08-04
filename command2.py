
import sys


def Addition(no1,no2):
    return no1+no2

def main():
    ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
    print("Additin of {} and {} is {}.".format(sys.argv[1],sys.argv[2],ret))
    




if __name__=="__main__":
    main()




# python command.py 11 21 31                                  
