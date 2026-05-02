# Выполнение дз на codewars

def greet(name):
    if name == "Johnny":
       return "Hello,my love!"
    else : return f"Hello,{name}!"

print(greet("Johnny"))
print(greet("Jenny"))


def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello,{name}!" 

########################################################

def distance(x1, y1, x2, y2):
     import math
     distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    
     return round(distance,2)


#################################################

def filter_words(st):
    v = st.split() 
    st = " ".join(v) 
    print(st) 

    return st.capitalize() 


print(filter_words("WOW this is REALLY          amazing"))

# ###########################################

def filter_words(st):
     print(st)
     return st.capitalize()


def number_to_string(num): #функция → название → переменная
     print (str(num)) #Выведи мне число
     return str(num) #Верни число но в виде tuple через пробел

print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))

####################

def reverse(st):
      print( f"We must reversal string {st}")
      new_def = st.split()
      return st.reverse()
    

print(reverse("Hello world"))
print(reverse("Vibe coding - bad"))

####################################

def reverse_list(l):
     print(l) 
     l.reverse()

     return l

#######################################

def solution(number):
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(solution(23))
print(solution(15))