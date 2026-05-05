import random

result = random.randint(1, 100)
guess_tries = []

def numb_guess(guess):
    for val in range(10):
        if guess < result:
            guess_tries.append(guess)
            print(f"Your previous attemps: {guess_tries}")
            return f"the number {guess} is low!"
        elif guess > result:
            guess_tries.append(guess)
            print(f"Your previous attemps: {guess_tries}")
            return f"the number {guess} is high!"
        else:
            print(guess)
            return f"Congratulation! The number is: {result}"
    

for val in range(10):
    guess = int(input("Enter a number between 1 and 100: "))
    
    if not (1 <= guess <= 100):
        print("Invalid number.")
        continue

    print(numb_guess(guess))

    if guess == result:
        break
else:
    print(f"Game over! The number was: {result}")
