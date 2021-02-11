try:
    a=open('apple.txt','a')
    b=input("\n enter a colour:")
    while b:
        a.write(b+"\n")
        b=input("enter a colour:")
    a.close()
except IOError as e:
    print(e)