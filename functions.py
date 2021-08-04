

#function accepts nothing and return nothing
def fun():
    print("function fun")
    
# functions accepts parameter and return nothing
def gun(no):
    print("function gun with parameter:",no)
    
# functions accepts parameter and return the value
    
def sun(no):
    print("function sun with parameter:",no)
    return no+1
    
 #function accepts multiple value and return multiple values   
def Addsum(no1,no2):
    add = no1+no2
    sub = no1-no2
    return add,sub
    
# nested function defination
def marvellous():
    print("inside marvellous")
    def infosystem():
        print("inside infosystem")
    infosystem()
    infosystem()

    
def main():
    fun()
    gun(11)
    ret = sun(10)
    print("return value of sun is:",ret)
    
    
    ret1,ret2 = Addsum(12,10)
    print("addition is:",ret1)
    print("substrin:",ret2)

    marvellous()
if __name__=="__main__":
    main()