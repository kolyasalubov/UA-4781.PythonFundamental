def rectangle_area() -> int:
    """
    Docstring for rectangle_area
    This function calculates the area of a rectangle
    Output: int
    """
    length = int(input("Writhe the length: "))
    width = int(input("Write the width: "))
    print(length * width)


def triangle_area():
    """
    Docstring for triangle_area
    This function calculates the area of a triangle
    Input: 
    Output: float
    """
    base = int(input("Writhe the base: "))
    height = int(input("Write the height: "))
    print(round((base*height)/2,2))


def circle_area():
    """
    Docstring for circle_area
    This function calculates the area of a circle
    Input: 
    Output: float
    """
    PI = 3.14
    radius = int(input("Writhe the radius: "))
    print((radius**2)*PI)

choice = input("Choose a shape: \n1 - rectangle;\n2 - triangle;\n3 - circle;\n ")

if choice == '1':
    rectangle_area()
elif choice == '2':
    triangle_area()
elif choice == '3':
    circle_area()
else:
    print("Wrong input")
