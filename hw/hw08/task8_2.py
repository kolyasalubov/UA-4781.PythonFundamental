import math

def rectangle_area(a, b):
    return a * b

def triangle_area(h, a):
    return 0.5 * h * a

def circle_area(r):
    return math.pi * math.pow(r, 2)

print("Вітаю! Я допоможу порахувати площу фігури.")
print("Виберіть варіант:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Коло")

choice = input("Ваш вибір (1/2/3): ")

if choice == '1':
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    print(f"Площа: {rectangle_area(a, b)}")

elif choice == '2':
    h = float(input("Введіть висоту h: "))
    a = float(input("Введіть основу a: "))
    print(f"Площа: {triangle_area(h, a)}")

elif choice == '3':
    r = float(input("Введіть радіус r: "))
    print(f"Площа: {circle_area(r)}")

else:
    print("Невірний вибір. Спробуй ще раз.")