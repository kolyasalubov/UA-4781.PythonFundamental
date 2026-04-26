def area_of_rectangle(w, h):
    return w * h
   
def area_of_triangle(b, h):
    return 0.5 * b * h

def area_of_circle(r):
    return 3,14 * r * r

print("Choose shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    w = float(input("Width: "))
    h = float(input("Height: "))
    print("Area of rectangle:", area_of_rectangle(w, h))

elif choice == "2":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area of triangle:", area_of_triangle(b, h))

elif choice == "3":
    r = float(input("Radius: "))
    print("Area of circle:", area_of_circle(r))

else:
    print("Invalid choice")
