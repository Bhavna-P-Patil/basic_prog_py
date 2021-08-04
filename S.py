from sys import *

def Function(value):
    print("Inside function with parameter:"+value)

def main():
    print("------Marvellous-------")
    print("Script Title:"+argv[0])

    if(len(argv)!=2):
        print("Insufficient arguments to the script")
        exit()

    if(argv[1]=="-u"):
        print("Use the script as Name.py parameters")
        exit()

    if(argv[1]=="-h"):
        print("This is Demo automation script")
        exit()
    Function(argv[1])

if __name__=="__main__":
    main()