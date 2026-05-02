import math

def cirlce_function (R):
     return math.pi * R **2

def triangle_function (a,h):
     return (a*h)/2

def rectangle_function(a,b):
    return a*b


user = int(input())
if user == 1:
     R= float(input("Введите радиус:"))
     print(cirlce_function(R))
elif  user == 2:
     a = int(input("Введите сторон"))
     h = int(input("Введите введите высоту"))
     print(triangle_function(a,h))
else :
     a = int(input("Введите длину прямоугольника "))
     b = int(input("Введите ширину прямоугольника "))
     print(rectangle_function(a,b))