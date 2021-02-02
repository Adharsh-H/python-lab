import graphics.rectangle as rec
from graphics.circle import area as a,perimeter as p
import graphics.dgraphics.cuboid as cub
from graphics.dgraphics.sphere import*
print("***********RECTANGLE**********")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("AREA=",rec.area(l,b))
print("PERIMETER=",rec.perimeter(l,b))
print("\n***********CIRCLE**********")
r=int(input("enter the radius:"))
print("AREA=",a(r))
print("CIRCUMFERENCE=",p(r))
print("\n***********CUBOID**********")
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
print("AREA=",cub.area(l,b,h))
print("PERIMETER=",cub.perimeter(l,b,h))
print("\n***********SPHERE**********")
r=int(input("enter the radius:"))
print("AREA=",area(r))
print("CIRCUMFERENCE=",perimeter(r))