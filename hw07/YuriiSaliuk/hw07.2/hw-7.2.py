def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
    
###############################################

def distance(x1, y1, x2, y2):
    res = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)
    return res 

###############################################

def filter_words(st):
    res = " ".join(st.split())
    return res.capitalize()

###############################################

def number_to_string(num):
    num = str(num)
    return num

###############################################

def reverse(st):
    rozb = st.split()
    res = " ".join(rozb[::-1])
    return res

###############################################

def reverse_list(l):
    res = l[::-1]
    return res

###############################################

def solution(number):
    if number < 0: 
     return 0
    dep = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            dep += i
    return dep          
        
###############################################

def zero_fuel(distance_to_pump, mpg, fuel_left):
    mxdistance = mpg * fuel_left
    if mxdistance >= distance_to_pump:
     return True
    else: 
     return False

###############################################

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
     return name + " plays banjo"
    else:
     return name + " does not play banjo" 
    
###############################################
    
def bool_to_word(boolean):
    if boolean == True:
     return 'Yes'
    else:
     return 'No'
    
###############################################

def count_sheeps(sheep):
  counter = 0
  for i in sheep:
     if i == True:
        counter += 1
     else:
        counter += 0 
     return counter    
  




