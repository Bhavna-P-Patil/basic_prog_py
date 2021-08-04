#MultiInheritance

class Base1:
    def __init__(self):
        print("inside base1 constructor")
    def fun(self):
        print("Inside Base1 fun")


class Base2:
    def __init__(self):
        print("inside base2 constructor")
    def fun(self):
        print("Inside Base2 fun")

class Derived(Base1,Base2):
    def __init__(self):
      Base1.__init__(self)
      Base2.__init__(self)
      print("Inside Deriverd constructor")
    def fun(self):
        print("Derived fun")


def main():
    dobj = Derived()
    dobj.fun()

if __name__=="__main__":
    main()