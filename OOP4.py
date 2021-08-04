# OOP approach paradigm

class Arithmatic:                      # Class defination
    value =111                         # class variable
    def __init__(self,i,j):            # class constuctor
        print("inside constructor")
        self.no1 = i                   # class instance variable
        self.no2 = j                   # instance variable


    def Add(self):                     # instance method
        print(Arithmatic.value)
        return self.no1 + self.no2


    def Sub(self):                     # instance method
        return self.no1-self.no2





def main():
    print("value is",Arithmatic.value)
    obj1=Arithmatic(21,11)             #__init__(obj1, 21,11)  
    obj2=Arithmatic(101,51)            #__init__(obj2,101,51)

    ret = obj1.Add()                   # ret= Add(obj1)
    print("addition is",ret)           
    ret = obj1.Sub()                   # ret= Sub(obj1)
    print("substraction is",ret)
    
    print("value is",obj1.value)

    ret = obj2.Add()                   # ret= Add(obj2)
    print("addition is",ret)
    ret = obj2.Sub()                   # ret= Sub(obj2)
    print("substraction is",ret)

if __name__=="__main__":
    main()
