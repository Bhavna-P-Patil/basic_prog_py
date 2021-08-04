def main():
    name = input("Enter the file name ")

    fobj = open(name,"w")               # create new file
    size = int(input("enter no of charectors to read"))

    print("data from file is")
    print(fobj.read(size))
if __name__=="__main__":
    main()