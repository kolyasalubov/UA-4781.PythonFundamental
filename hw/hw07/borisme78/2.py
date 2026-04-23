# Task2. Write a program that calculates the area of rectangle, triangle, and circle.(write three functions to calculate the area. And call them in the main program depending on the user's choice).
import math

def area_rectangle(length, width):
    """
    This function calculates the area of a rectangle given its length and width.
    """
    return length * width

def area_triangle(base, height):
    """
    This function calculate the area of triangle given its base and height.
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    This function calculates the area of a circle given its radius.
    """
    return math.pi * radius ** 2

def main():
    """
    This function calculates the area based on the user's selection
    Choice1: area of a rectangle
    Choice2: area of a triangle
    Choice3: area of a circle
    """
    
    print("Calculating area:\n1.Rectangle\n2.Triangle\n3.Circle")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of the rectangle is:", area_rectangle(length, width))
    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area of the triangle is:", area_triangle(base, height))
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle is:", area_circle(radius))
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
# Verification of the function
if __name__ == "__main__":
    main()