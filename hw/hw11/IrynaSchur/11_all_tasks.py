def checknumbers():
    try:
        age = int(input())
        check_age(age)
        print(age)
    except:
        checknumbers()
checknumbers()

def check(login):
    try:
        s = login.lower()

        if "admin" in s:
            role = "admin"
        elif "employee" in s:
            role = "employee"
        else:
            raise ValueError

        digits = ''.join(ch for ch in s if ch.isdigit())
        if digits == "" or int(digits) <= 0:
            raise ValueError

        return True

    except:
        raise ValueError(f"incorrect login '{login}'")
    

class InputError(Exception):
    def __init__(self, data):
        self.data = data


def check(value):
    if not isinstance(value, str):
        raise InputError("Type text error")
    
    if len(value) < 3:
        raise InputError("Short text error")
    
    if len(value) > 15:
        raise InputError("Long text error")
    
    return True

def check_odd_even(number):
    try:
        if number % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except:
        return "You entered not a number."


class MyError(Exception):
    def __init__(self, number):
        self.number = float(number)

    def __str__(self):
        return f"You input negative number: {self.number}. Try again."


def check_positive(number):
    try:
        number = float(number)

        if number >= 0:
            return f"You input positive number: {number}"
        else:
            return MyError(number)

    except ValueError:
        return "Error type: ValueError!"
    
def divide(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError
        
        result = numerator / denominator
        return f"Result is {result}"
    
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    
    except ValueError:
        return "Value Error! You did not enter a number!"