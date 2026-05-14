# Task1. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
######################################################## 

# Task2. Area of a shape
import math
def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(d, 2)
########################################################

# Task3.No yelling!
def filter_words(st):
    return " ".join(st.split()).capitalize()
########################################################

# Task4. Convert a Number to a String!
def number_to_string(num):
    return str(num)
########################################################

# Task5. Reversing Words in a String.
def reverse(s):
    words = s.split()
    return " ".join(words[::-1])
########################################################

# Task6. Reverse List Order.    
def reverse_list(l):
    return l[::-1]
########################################################

# Task7. Multiples of 3 or 5.
def solution(number):
    if number < 0:
        return 0
    return sum(a for a in range(number) if a % 3 == 0 or a % 5 == 0)
########################################################

# Task8. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
#######################################################

# Task9. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
#########################################################

# Task10. Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
##########################################################

# Task11. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)
##########################################################

# Task12. Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False
