from random import randint

rnd = randint(1, 100)

for i in range(10):
    numb = int(input('Enter your number:'))
    if numb == rnd:
        print('You win')
        break
    else:
        if numb > rnd:
            print('Your number is higher than rnd number') 
        else:
            print('Your number is lower than rnd number') 
else:
    print('You lose')
      