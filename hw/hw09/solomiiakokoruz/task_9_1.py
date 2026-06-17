import random

secret_number = random.randint(1, 100)
attempts = 10

print("Guess the number from 1 to 100 in 10 tries")

for i in range(1, attempts + 1):
    guess = input("Enter a number: ")
    
    if guess.isdigit():
        guess = int(guess)
        
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("You guessed it!")
            break
    else:
        print("That's not a number")
        
    if i == attempts:
        print("You lost. The number was:", secret_number)