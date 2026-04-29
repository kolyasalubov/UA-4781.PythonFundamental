print("codewars")

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

######################################################

import math

def distance(x1, y1, x2, y2):
    return round(math.sqrt(((x2-x1)**2)+((y2-y1)**2)),2)

######################################################

def filter_words(st):
    clear = " ".join(st.split())
    return clear.capitalize()

######################################################

def number_to_string(num):
    return str(num)

######################################################

def reverse(st):
    l = st.split()
    l.reverse()
    st = " ".join(l)
    return st

######################################################

def reverse_list(l):
    l.reverse()
    return l

######################################################

def solution(number):
    sum = 0
    l = list(range(number))
    for i in l:
        if (i%3==0 or i%5==0) and i>0:
            sum += i
    return sum

######################################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump

######################################################

def are_you_playing_banjo(name):
    ans = ""
    if name.startswith(("R","r")):
        ans = f"{name} plays banjo"
    else:
        ans = f"{name} does not play banjo"
    return ans

######################################################

def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

######################################################

def count_sheeps(sheep):
    counter = 0 
    for i in sheep:
        if i is True and not None:
            counter += 1
    return counter 

######################################################

def correct_tail(body, tail):
    sub = body[len(body)-len(tail):]
    if sub == tail:
        return True
    else:
        return False
