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
    
    s = math.pi * math.pow(radius, 2)
    return s