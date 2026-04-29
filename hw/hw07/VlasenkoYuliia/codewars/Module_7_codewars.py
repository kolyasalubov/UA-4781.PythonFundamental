
# #I. Jenny's secret message
# def greet (user):

#     if user == 'Johnny':
#         print(f"Hello my lovly, {user}") 
#     else:
#         print(f"Hello, {user}. I'm happy to see you")

# greet("Yuliia")
# greet("Johnny")


def greet(name):
    if name == 'Johnny':
        return f"Hello, my love!"
    return f"Hello, {name}!"
####################################################

#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    from math import sqrt
    c = sqrt(dx**2 + dy**2)
    return round(c, 2)

####################################################

#III. No yelling!
def filter_words(st):
    st1 = st[0].upper()
    st2 = st[1:].lower() 
    st3 = (st1 + st2).split()
    return ' '.join(st3)

#######################################

#IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

#######################################

# V. Reversing Words in a String
def reverse(st):
    st = st.split()
  
    return ' '.join(st[::-1])

#######################################

#VI. Reverse List Order
def reverse_list(l):
  l.reverse()
  return l

#######################################

#VII. Multiples of 3 or 5
def solution(number):
    new_list = []
    if number < 0:
        return 0
    else:
        for val in range(number):
            if val%5 == 0 or val%3 == 0:
                new_list.append(val)
    return sum(new_list)

#######################################

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_total = mpg*fuel_left
    return distance_to_pump <= distance_total
    
#######################################

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r': 
        return name + " plays banjo" 
    return name + " does not play banjo"

#######################################

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if bool(boolean):
        return "Yes"
    return "No"

#######################################

#XI. Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)

#######################################

#XII. Is this my tail?
def correct_tail(body, tail):
    if body[-1]== tail:
        return True
    return False