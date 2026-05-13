import math

def rectangle_area(width, length):
    '''
    Return the area of a rectangle.
    '''
    return width * length

def triangle_area(side1, side2, side3):
    '''
    Return the area of a triangle.
    '''
    p = (side1 + side2 + side3) / 2
    s = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return s

def circle_area(radius):
    '''
    Return the area of a circle.
    '''
    PI = 3.14
    s = PI * radius ** 2
    return s



print("Choose one of 3 shapes: rectangle, triangle, circle")
choice = input()
if choice == "rectangle":
    print("Enter width and length:")
    width = float(input())
    length = float(input())
    print(round(rectangle_area(width, length),2))
elif choice == "triangle":
    print("Enter numbers for each side")
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    print(round(triangle_area(side1, side2, side3), 2))
elif choice == "circle":
    print("Enter radius")
    radius = float(input())
    print(round(circle_area(radius), 2))
else:
     print("You can put only one of these shapes: rectangle, triangle, circle")






