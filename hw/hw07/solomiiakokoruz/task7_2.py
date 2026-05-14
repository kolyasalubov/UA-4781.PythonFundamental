import math
def area_rectangle(a, b):
    """Calculate the area of a rectangle.
    Parameters: a: length, b: width"""
    return a * b

def area_triangle(a, h):
    """Calculate the area of a triangle.
    Parameters: a: base, h: height"""
    return round(0.5 * a * h, 2)

def area_circle(r):
    """Calculate the area of a circle from its radius.
    Parameters: r: radius"""
    return round(math.pi * r**2, 2)

print("Choose the shape to calculate the area:")
print("1. This is a rectangle")
print("2. This is a triangle")    
print("3. This is a circle")

choice = input("Enter the number of the shape: ")

if choice == "1":
    a = (input("Enter the length of the rectangle: "))
    b = (input("Enter the width of the rectangle: "))
    if a.isdigit() and b.isdigit():
        print(f"Area: {area_rectangle(int(a), int(b))}")
    else:
        print("Error: please enter numbers.")

elif choice == "2":
    a = (input("Enter the base of the triangle: "))
    h = (input("Enter the height of the triangle: "))
    if a.isdigit() and h.isdigit():
        print(f"The area of the triangle is: {area_triangle(int(a), int(h))}")
    else:
        print("Error: please enter numbers.")

elif choice == "3":
    r = (input("Enter the radius of the circle: "))
    if r.isdigit():
        print(f"The area of the circle is: {area_circle(int(r))}")
    else:
        print("Error: please enter a number.")
