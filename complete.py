# Defination of addition function
def Addition(no1,no2):
  ans = no1+no2
  return ans


# Defination of multiplication function
def Multiplication(no1,no2):
  ans = no1*no2
  return ans

#Start 26 27 12 -> 19 2 20 7 20 22 23 27 End
#Entry point function
def main():
  print("Enter first number:")
  value1 = int(input())

  print("Enter second number:")
  value2 = int(input())

  ret1 = Addition(value1,value2)
  ret2 = Multiplication(value1,value2)

  print("Addition is:",ret1)
  print("Multiplication:",ret2)



#code starter
if __name__=="__main__":
   main()
