import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * r ** 2


def main():
    print("Оберіть фігуру:")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")

    choice = input("Ваш вибір: ")

    if choice == "1":
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        print("Площа:", rectangle_area(a, b))

    elif choice == "2":
        h = float(input("Введіть висоту: "))
        a = float(input("Введіть основу: "))
        print("Площа:", triangle_area(h, a))

    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа:", circle_area(r))

    else:
        print("Невірний вибір")


if __name__ == "__main__":
    main()