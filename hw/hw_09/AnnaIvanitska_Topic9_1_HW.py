import random

my_number = random.randint(1,100)

guess = int(input("Enter your guess: "))

attempts = 1

while attempts < 10:
    print(f"You have {10 - attempts} attempts left")
    guess = int(input("Enter your guess: "))
    if guess > 100 or guess < 1:
        print("Your number is out of 1 to 100 range")
    elif guess > my_number:
        print("Your number is bigger than provided one")
    elif guess < my_number:
        print("Your number is smaller than provided one")
    else:
        print(f"You've guessed. Number is {my_number}")
    attempts += 1


