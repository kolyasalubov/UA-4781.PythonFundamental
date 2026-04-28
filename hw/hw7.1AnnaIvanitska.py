#Task 1

def return_max(a,b):
    '''This function returns the maximum of two numbers'''
    return max(a,b)

print(return_max(23,45))


#Task 2
import math

def geomr_fig():
    '''This function returns the area of rectangle, circle and triangle'''
    print("Choose the figure: 1 - rectangle, 2 - circle, 3 - triangle")
    figure = int(input())
    if figure == 1:
        print("Enter the length and width of rectangle: ")
        lenght = float(input("Length: "))
        width = float(input("Width: "))
        rectangle = lenght * width
        print(rectangle)
    elif figure ==2:
        print("Enter the radius of a circle: ")
        radius = float(input("Radius: "))
        circle = math.pi * radius**2
        print(circle)
    elif figure ==3:
        print("Enter the base and the height of a triangle: ")
        base = float(input("Base: "))
        height = float(input("Height: "))
        triangle = 1/2 * base * height
        print(triangle)
    else: 
        print("Wrong choice")
print (geomr_fig())


#Task 3

def calc_number_of_characters():
    '''This function returns the number of characters in a string'''
    string = input("Enter a string: ")
    unique = set(string)
    freq = {}
    for x in unique:
        freq[x] = string.count(x)
    return freq
print(calc_number_of_characters())
