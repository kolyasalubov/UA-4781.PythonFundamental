from area_function import *



def main():
    print("Виберіть операцію:")
    print("1. Визначити площу прямокутника")
    print("2. Визначити площу трикутника")
    print("3. Визначити площу кола")
    operation = input("Виберіть операцію (1, 2, чи 3): ")

    if operation == "1":
        num1 = get_float("Введіть ширину: ")
        num2 = get_float("Введіть довжину: ")
        print(f"Площа прямокутника: {area_rectangle(num1, num2)}")
    elif operation == "2":
        num1 = get_float("Введіть основу: ")
        num2 = get_float("Введіть висоту: ")
        print(f"Площа трикутника: {area_triangle(num1, num2)}")
    elif operation == '3':
        num1 = get_float("Введіть радіус: ")
        print(f"Площа кола: {area_circle(num1)}")
    else:
        print("Введіть число (1, 2, чи 3)")
        return main()
 

if __name__ == '__main__':
    main()