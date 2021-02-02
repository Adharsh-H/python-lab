from calendar import month
import datetime
y=int(input("enter the year:"))
m=int(input("enter the month[1-12]:"))
print("calendar of year",y,"month",m,"is\n\n",month(y,m))
c=int(input("enter the date[1-31]:"))
d=datetime.datetime(y,m,c)
print("Year is ",d.strftime("%Y"))
print("Month  is ",d.strftime("%B"))
print("Day is ",d.strftime("%A"))
print("Date in format(MM/DD/YY) is ",d.strftime("%x"))
e=datetime.datetime.now()
print("Now the time is ",e.strftime("%X"))