def max_of_two(a, b):
    """
    Returns the largest of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: The larger number
    """
    return a if a > b else b

import math

def rectangle_area(length, width):
    """Returns the area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Returns the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Returns the area of a circle."""
    return math.pi * radius ** 2


# TASK 2
choice = input("Choose shape (rectangle/triangle/circle): ").lower()

if choice == "rectangle":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area:", rectangle_area(l, w))

elif choice == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", triangle_area(b, h))

elif choice == "circle":
    r = float(input("Enter radius: "))
    print("Area:", circle_area(r))

else:
    print("Invalid choice")

# TASK 3

def char_count(s):
    """
    Returns a dictionary with the count of each character in the string.

    Parameters:
    s (str): Input string

    Returns:
    dict: Character frequency
    """
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


# Example
print(char_count("hello"))