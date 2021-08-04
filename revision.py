
# Design object oriented python application which accepts N numbers from users and
# perform below operations
# Display all even numbers
# calculate the summation of all numbers
# Display all perfect numbers

class Numbers:

    


    def __init__(self,no=10):
       self.size=no
       self.arr=[]

    def __del__(self):
        print("dealocating the memory of object")
        del self.arr


       

    def Accept(self):
        print("please enter the elements")
        for i in range(self.size):
            print("enter number:",i+1)
            self.arr.append(int(input()))
        
    def Display(self):
        print("elements of list are")
        for i in range(self.size):
            print(self.arr[i])

    def summation(self):
        sum=0
        for i in range(self.size):
            sum=sum+self.arr[i]
            
        return sum

    def EvenDisplay(self):
        print("even elements from list are:")
        for i in range(self.size):
            if(self.arr[i]%2)==0:
                print(self.arr[i])


    def perfectDisplay(self):
        sum=0
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)):
                if (self.arr[i]%j)==0:
                    sum=sum+j
            if sum==self.arr[i]:
                print(self.arr[i])
            sum=0



    def primeDisplay(self):
         flag = False
         for i in range(self.size):
             for j in range(2,int(self.arr[i]/2)+1):
                 if(self.arr[i]%j)==0:
                     flag=True
                     break
             if flag==False:
                  print(self.arr[i])
             flag= False    

def main():
    print("enter number of elements")
    value =int(input())


    obj1 =Numbers(value)
    obj1.Accept()
    obj1.Display()
    ret= obj1.summation()
    print("summation of all elements ",ret)
    obj1.EvenDisplay()
    print("perfect number are:")
    obj1.perfectDisplay()
    print("prime numbers are")
    obj1.primeDisplay()

    del obj1




if __name__=="__main__":
    main()
