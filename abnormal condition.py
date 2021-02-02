a=int(input("enter a number:"))
try:
    if not(a>=90 and a<=120):
        raise ValueError ('Abnormal Condition')
except ValueError as e:
    print(e) 
else:
    print("value is between 90-120")       