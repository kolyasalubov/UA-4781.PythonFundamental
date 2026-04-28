import math
def area_rectangle(length, width):
    return length * width
def area_triangle(base, height):
    return 0.5 * base * height
def area_circle(radius):
    return math.pi * radius ** 2

def main():
    print("Програма для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    choice = input("Виберіть фігуру (введіть 1, 2 або 3): ")
    if choice == '1':
        l = float(input("Введіть довжину: "))
        w = float(input("Введіть ширину: "))
        print(f"Площа прямокутника: {area_rectangle(l, w)}")
    elif choice == '2':
        b = float(input("Введіть основу трикутника: "))
        h = float(input("Введіть висоту трикутника: "))
        print(f"Площа трикутника: {area_triangle(b, h)}")
    elif choice == '3':
        r = float(input("Введіть радіус кола: "))
        print(f"Площа кола: {area_circle(r):.2f}")

    else:
        print("Помилка: невірний вибір. Будь ласка, запустіть програму знову.")
if __name__ == "__main__":
    main()