#positional arguments
def Student(name,rno,address,marks):
    print("Name is:",name)
    print("Roll no is:",rno)
    print("Address is:",address)
    print("Marks is:",marks)


# keyword arguments
#def Computer(RAM,Processor,HDD):
 #   print("Ram size is:",RAM)
  #  print("processor name is:",Processor)
   # print("size of HDD is:",HDD)


#default argument(shoudld be right to left order)
def CircleArea(radius,PI=3.14):
    print("value of PI is:",PI)
    return PI*radius*radius    
    
    
    
#variable number of arguments
def fun(*value):
    print("Numbers of arguments are:",len(value))    




def main():
    Student("Bhavna",12,"jalgaon",65)
    #Computer(processor="i7",RAM=8,HDD="1TB")
    CircleArea(10.25)
    CircleArea(10.25,7.12)
    fun(10,20,30)
    fun()


if __name__=="__main__":
    main()
