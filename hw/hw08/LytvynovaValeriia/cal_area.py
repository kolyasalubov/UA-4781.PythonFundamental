from math import pow, pi

def rectangle_area() -> int:
    """
    Docstring for rectangle_area
    This function calculates the area of a rectangle
    Output: int
    """
    length = int(input("Writhe the length: "))
    width = int(input("Write the width: "))
    return length * width


def triangle_area():
    """
    Docstring for triangle_area
    This function calculates the area of a triangle
    Input: 
    Output: float
    """
    base = int(input("Writhe the base: "))
    height = int(input("Write the height: "))
    return round(0.5 * (height * base), 2)


def circle_area():
    """
    Docstring for circle_area
    This function calculates the area of a circle
    Input: 
    Output: float
    """
    radius = int(input("Writhe the radius: "))
    return round((pow(radius,2))*pi,2)
