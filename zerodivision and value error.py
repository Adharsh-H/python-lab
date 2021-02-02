try:
    a=int(input("enter number a:"))
    b=int(input("enter number b:"))
    print(a/b)
except(ZeroDivisionError,ValueError) as e:
    print(e)  
else:    
    
    print("division successful")
