#1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#2

def distance(x1, y1, x2, y2):
    # Your code 
    dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.50
    return round(dist, 2)

#3

def filter_words(st):
    st = " ".join(st.split())
    return st.capitalize()
    pass

#4

def number_to_string(num):
    return str(num)
    pass

#5

def reverse(st):
    words = st.split()
    st = words[::-1]
    st = " ".join(st)
    return st

#6

def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

#7

def solution(number):
    if number < 0:
        return 0
    
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#8 

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False
    
#9

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo" 
    # Implement me!
    return name + " does not play banjo"

#10

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#11

def count_sheeps(sheep):
    return sheep.count(True)

#12

def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False