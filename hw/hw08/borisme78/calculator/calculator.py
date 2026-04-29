import operation


def main():
    print("Виберіть операцію:")
    print("1. Додавання: ")
    print("2. Віднімання: ")
    print("3. Множення: ")
    print("4. Ділення: ")

    choise = input("Введіть номер операції: ")

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Введіть число")

    if choise == "1":
        print(f"Результат: {operation.add(num1, num2)}")
    elif choise == "2":
        print(f"Результат: {operation.subtract(num1, num2)}")
    elif choise == "3":
        print(f"Результат: {operation.multiply(num1, num2)}")
    elif choise == "4":
        print(f"Результат: {operation.divide(num1, num2)}")
    else:
        print("Невірний вибір операції")


if __name__ == "__main__":
    main()
