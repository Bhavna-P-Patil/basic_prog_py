

i=1               # define the variable


def fun():
    global i      # declare the variable
    
    print(i)
    i=i+1
    fun()


def main():
    fun()
    

if __name__ =="__main__":
    main()
