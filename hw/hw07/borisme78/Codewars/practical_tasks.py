#############################################

def greet(name):
    
    if name == "Johnny":
        return "Hello, my love!"
    
    return "Hello, {name}!".format(name=name)

##############################################

import math
def distance(x1, y1,x2, y2):
    x = (x2 + x1)**2
    y = (y2 - y1)**2
    result = math.sqrt(x + y)
    return round(result, 2)


##############################################

def filter_words(st):
    low_st = st.lower()
    first_latter_is_upper = low_st.capitalize()
    result = " ".join(first_latter_is_upper.split())
    return result

###############################################

def number_to_string(num):
    num_str = str(num)
    return num_str

###############################################

def reverse(st):
    """
    Розвертає порядок слів у рядку.
    
    Метод розбиває рядок на слова (ігноруючи зайві пробіли), 
    змінює їхній порядок на зворотний і збирає назад у рядок.
    """
    words = st.split()[::-1]
    result = " ".join(words)
    return result


################################################

def reverse_list(l):
    l.reverse()
    return l

################################################

def solution(number):
    sum = 0 
    if number < 0:
        return 0
    numbers = list(range(1, number))
    for i in numbers:
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i    
    return sum

####################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False
# Verification of the function
print(zero_fuel(50, 30, 2))

#####################################

def are_you_playing_banjo(name):
    name_lower = name.lower()
    if name_lower[0] == "r":
        return name + " plays banjo"
    else:        
        return name + " does not play banjo"
# Verification of the function
print(are_you_playing_banjo("Ringo"))
print(are_you_playing_banjo("john"))

#####################################

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:       
        return "No"
# Verification of the function
print(bool_to_word(True))
print(bool_to_word(False))

#####################################

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count 

#######################################

def correct_tail(body, tail):
    sub = body[::-1]
    sub_first = sub[0]
    if sub_first == tail:
        return True
    else:
        return False

#######################################