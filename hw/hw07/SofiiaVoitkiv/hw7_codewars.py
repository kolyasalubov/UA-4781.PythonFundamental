#### Task 1. Jenny's secret message.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return (f"Hello, {name}!")
    
#### Task 2. Find The Distance Between Two Points.

import math
def distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return round(d, 2)

#### Task 3. No yelling!

def filter_words(st):
    a = st.split()
    b = " ".join(a)
    result = b.lower()
    return result.capitalize()

#### Task 4. Convert a Number to a String!

def number_to_string(num):
    string = str(num)
    return string

#### Task 5. Reversing Words in a String.

def reverse(st):
    st = st.split()  
    st.reverse()
    return " ".join(st)

#### Task 6. Reverse List Order.

def reverse_list(l):
    l.reverse()
    return l

#### Task 7. Multiples of 3 or 5.

def solution(number):
    b = 0
    if number < 0:
        b = 0
    else:
        for a in range(number):
            if a % 3 == 0 or a % 5 == 0:
                b += a
    return b

#### Task 8. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
    
#### Task 9. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"  
    else:
        return f"{name} does not play banjo"
    
#### Task 10. Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    return "No"

#### Task 11. Counting sheep...

def count_sheeps(sheep):
    total = 0
    for present in sheep:
        if present == True:
            total += 1
    return total

#### Task 12. Is this my tail?

def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    return False



