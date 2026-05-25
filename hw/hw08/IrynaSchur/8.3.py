from math import pi, pow
import areas

figure = input("Enter figure (rectangle, triangle, circle): ")

if figure == "rectangle":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print(areas.rectangle(a, b))

elif figure == "triangle":
    a = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(areas.triangle(a, h))

elif figure == "circle":
    r = float(input("Enter radius: "))
    print(areas.circle(r))

else:
    print("Unknown figure")