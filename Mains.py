# function definition
def oddeven(num):
    resu = num % 2
    if (resu == 0):
        print("%d is eve!" %(num))
    else:
        print("%d is od!" %(num))
  
num = int(input("Please Enter A Number: "))
oddeven(num)
