# Task 2.1 Area of a rectangle
def rectangle_area(width, length):
    area = width * length
    return f"The area of a rectangle is {area} m²"


# Task 2.2 Area of a triangle
#Формула площі трикутника за стороною та висотою
def area_triangle(base, height):
    area = (base * height)/2
    return f"The area of a triangle is {area}"


# Task 2.3 Area of a circle with radius 
import math
def area_circle(radius):
    area = math.pi*radius**2
    return f"The area of a circle with radius {radius} is {area:.2f}"
print(area_circle(4))

while True:
    print("*"*20) 
    print("Area formulas for geometric shapes:")
    print("1 - rectangle, 2 - triangle, 3 - circle, 0 - to exit")
    
    shape = int(input("Select your shape or exit: " '\n'))
    if shape == 0:
        print("Exit")
        break

    elif shape == 1:
         width = int(input("Please enter width (meters): " '\n'))
         length = int(input("Please enter length (meters): " '\n'))
         print(rectangle_area(width, length))
    elif shape == 2:
         base = int(input("Please enter base): " '\n'))
         height = int(input("Please enter height): " '\n'))
         print(area_triangle(base, height))
    elif shape == 3:
         radius = int(input("Please enter radius): " '\n'))
         print(area_circle(radius))
    else:
        print("Please, enter shape throuth 1 to 3")



