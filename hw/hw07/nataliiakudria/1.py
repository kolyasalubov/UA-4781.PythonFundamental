def get_largest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
result = get_largest_number(15, 42)
print(f"Найбільше число: {result}")