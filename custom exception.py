class err(Exception): pass
try:
    name="ramu"
    pswrd="2021"
    a=input("enter username:")
    b=input("enter password:")
    if a== name and b== pswrd:
       print("login successfully")
    else:
        print("invalid username or password")
except err as e:
    print(e)       