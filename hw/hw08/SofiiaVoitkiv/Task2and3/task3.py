import task3_func

choice = input("Choose one of 3 shapes: rectangle, triangle, circle: ")
if choice == "rectangle":
    print("Enter width and length:")
    width = float(input())
    length = float(input())
    print(round(task3_func.rectangle_area(width, length),2))
elif choice == "triangle":
    print("Enter numbers for each side")
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    print(round(task3_func.triangle_area(side1, side2, side3), 2))
elif choice == "circle":
    print("Enter radius")
    radius = float(input())
    print(round(task3_func.circle_area(radius), 2))
else:
     print("You can put only one of these shapes: rectangle, triangle, circle")