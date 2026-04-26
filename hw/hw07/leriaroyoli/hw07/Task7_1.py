
#Task1
def bigger_num(x,y):
    """Returns the bigger of two numbers."""
    if x > y:
        return x
    else:
        return y
    

#Task2
import math

def area_rectangle(a, b):
    """Calculates the area of ​​a rectangle based on two sides"""
    return a * b

def area_triangle(a, h):
    """Calculates the area of ​​a triangle given the base and height"""
    return round(0.5 * a * h, 1)

def area_circle(r):
    """Calculates the area of ​​a circle from its radius"""
    return round(math.pi * r**2, 1)


def main():
    print("Which figure should you calculate the area of?")
    print("Available shapes: rectangle, triangle, circle")
    
    choice = input("Your choice: ").strip().lower()

    match choice:
        case "rectangle":
            side_a = float(input("Enter the side A: "))
            side_b = float(input("Enter the side B: "))
            print(f"The area of ​​the rectangle is equal to: {area_rectangle(side_a, side_b)}")

        case "triangle":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter height: "))
            print(f"The area of ​​the triangle is equal to: {area_triangle(base, height)}")

        case "circle":
            radius = float(input("Enter the radius of the circle: "))
            print(f"The area of ​​a circle is equal to: {area_circle(radius)}")

        case _:
            print("Error! You entered an unknown shape. Please try again.")


if __name__ == "__main__":
    main()


#Task3
def num_of_characters(string):
    """ This function calculates the number of characters in string"""
    counters={} # key - char, val = sum of chars
    for i in string:
        if i not in counters:
            counters[i] = 1 
        else:
            counters[i] += 1
    return counters



def num_of_characters2(string):
    """ This function calculates the number of characters in string"""
    result = {}
    for a in set(string):
        c = string.count(a)
        result[a] = c
    return result



