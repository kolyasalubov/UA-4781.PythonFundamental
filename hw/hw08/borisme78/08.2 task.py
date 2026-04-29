# Напишіть програму на Python для перевірки правильності пароля (введеного користувачем).
# Вимоги до пароля:
# Щонайменше 1 літера з діапазону [a-z] та 1 літера з діапазону [A-Z].
# Щонайменше 1 цифра з діапазону [0-9].
# Щонайменше 1 символ з набору [$#@].
# Мінімальна довжина — 6 символів.
# Максимальна довжина — 16 символів.


def check_valid_password(password):
    check_valid : list[bool] =[
        len(password) >= 6,
        len(password) <=16,
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in '$#@' for char in password),
        any(char.isupper() for char in password)
    ]

    if all(check_valid):
        print('The password is valid')
        return True
    else:
        print('The password is not valid')
        return False



password = str(input('Enter the password:'))
check_valid_password(password)