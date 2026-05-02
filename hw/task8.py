password = input("Введіть пароль: ")

if not (6 <= len(password) <= 16):
    print("Невірна довжина: пароль має бути від 6 до 16 символів.")
else:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True

    if not has_lower:
        print("Помилка: відсутня мала літера.")
    if not has_upper:
        print("Помилка: відсутня велика літера.")
    if not has_digit:
        print("Помилка: відсутня цифра.")
    if not has_special:
        print("Помилка: відсутній спеціальний символ ($#@).")
        
    if has_lower and has_upper and has_digit and has_special:
        print("Пароль валідний!")