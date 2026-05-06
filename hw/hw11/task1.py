class NegativeAgeError(Exception):
    """Власний виняток для від'ємного віку."""
    pass

def process_age(age):
    if age < 0:
        raise NegativeAgeError("Вік не може бути від'ємним числом!")
    
    if age % 2 == 0:
        return f"Ваш вік ({age}) — парне число."
    else:
        return f"Ваш вік ({age}) — непарне число."

try:
    user_input = int(input("Введіть ваш вік: "))
    result = process_age(user_input)
    print(result)
except ValueError:
    print("Помилка: будь ласка, введіть ціле число.")
except NegativeAgeError as e:
    print(f"Виник виняток: {e}")