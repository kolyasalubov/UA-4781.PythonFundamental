import random
secret_number = random.randint(1, 100)
attempts = 10

print("Привіт! Я загадала число від 1 до 100. У тебе є 10 спроб, щоб його вгадати.")
for i in range(1, attempts + 1):
    guess = int(input(f"Спроба {i}: Введи своє число: "))
    if guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"На жаль, спроби закінчилися. Загадане число було: {secret_number}")