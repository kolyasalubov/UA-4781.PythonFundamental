import math

def rectangle_area (width, height):
    """Площа прямокутника = ширина * висота."""
    return width * height

def triangle_area(base, height):
    """Площа трикутника = 1.2 * основа * висота."""
    return 0.5 * base * height

def circle_area (radius):
    """Площа кола = p * r^2"""
    return math.pi * radius ** 2

def main ():
    print("Оберіть фігуру:")
    print("1 - прямокутник")
    print("2 - трикутник")
    print("3 - коло")
    choice = input("Ваш вибір:")

    if choice == '1':
        w = float(input('Ширина:'))
        h = float(input('Висота:'))
        print(f"Площа = {rectangle_area(w, h):.2f}")
    elif choice == '2':
        b = float(input('Основа:'))
        h = float(input('Висота:'))
        print(f"Площа = {triangle_area(b, h):.2f}")
    elif choice == '3':
        r = float(input('Радіус:'))
        print(f"Площа = {circle_area(r):.2f}")
    else:
        print("Невірний вибір")
main()
    
