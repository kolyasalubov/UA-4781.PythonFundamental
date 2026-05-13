from random import randint

random_num = randint(1, 100)
attemts = 0
while attemts < 10:
    cust = int(input("Try your luck: "))
    if cust == random_num:
        print("You win!")
        break
    elif cust < random_num:
        print("More...")
    else: 
        print("Less...")
    attemts +=1
if attemts == 10 and cust!= random_num:
    print("You lose.")
    
