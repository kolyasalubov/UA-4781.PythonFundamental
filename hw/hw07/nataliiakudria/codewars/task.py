def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, " + name + "!"

###################################################

import math
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)

####################################################


def filter_words(st):
    return " ".join(st.split()).capitalize()
print(filter_words("HELLO CAN YOU HEAR ME"))              
print(filter_words("now THIS is REALLY interesting"))    
print(filter_words("THAT was EXTRAORDINARY!"))  

####################################################

def number_to_string(num):
    return str(num)

###################################################

def reverse(st):
    return ' '.join(st.split()[::-1])

####################################################

def reverse_list(l):
    return l[::-1]

###################################################

def solution(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#####################################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (mpg * fuel_left) >= distance_to_pump

#####################################################

def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
####################################################

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

####################################################

def count_sheeps(sheep):
  return sheep.count(True)

####################################################

def correct_tail(body, tail):
     return body.endswith(tail)