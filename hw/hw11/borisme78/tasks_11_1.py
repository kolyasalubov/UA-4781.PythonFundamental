'''
Task1

'''
class CustomError(Exception): 
    
    def __init__(self, data): 
      self.data = data
    

def age_even_or__odd(age: int):
    if age % 2 == 0:
        print('Age is even')
    else:
        print('Age is odd')

def negative_age(age):
    if age < 0:
        raise CustomError('Age cannot be negative')

try:
    age = int(input('Enter your age:'))
     
    negative_age(age)

    age_even_or__odd(age)

except ValueError as e :
    print(f'ValueError: {e}')

except CustomError as e:
    print('Error:', e.data)

else:
    print('The program is working properly')

finally:
    print('The program is closed')
##########################################

'''
Task2

'''

class CustomError(Exception):
    def __init__(self, data):
        self.data = data 

def analyzes_number(number: int ):
    days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
            5: 'Friday', 6: 'Saturday', 7: 'Sunday' }
    return days.get(number)

def validate_number(number: int):
    if number < 1 or number > 7:
        raise CustomError('Enter number between 1 and 7')



try:
    number = int(input('Enter number: '))
    validate_number(number)
    name_day = analyzes_number(number)
    print(name_day)

except ValueError as e:
    print(f'ValueError: {e}')

except CustomError as e :
    print('Error:', e.data)
    

else:
    print(f'Have a nice {name_day}')

finally:
    print('The program is closed')