import geometricarea
print("*"*20)
print("Area Calculator for Geometric Shapes")
print("1: Recrangle, 2: Triangle, 3: Circle" )

while True:
    shape = int(input("Please select your shape or O to exit:"))
    match shape:
        case 0:
            print("Exit")
            break

        case 1:
            width = float(input("Please enter width (meters): " '\n'))
            length = float(input("Please enter length (meters): " '\n'))
            print(f"The area of a rectangle is {geometricarea.rectangle_area(width, length)} m²")
        case 2: 
            base = float(input("Please enter base: " '\n'))
            height = float(input("Please enter height: " '\n'))
            print(f"The area of a triangle is {geometricarea.area_triangle(base, height)}")
        case 3:
            radius = float(input("Please enter radius: " '\n'))
            print(f"The area of a circle is {geometricarea.area_circle(radius):.2f}")
        case _:
            print("Please, enter shape throuth 1 to 3")
    

        
        
