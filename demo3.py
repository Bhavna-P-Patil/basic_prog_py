def main():
    name = input("Enter the file name that you want to create")

    fobj = open(name,"w")               # create new file


    print("data from file is")
    print(fobj.read(size))
if __name__=="__main__":
    main()