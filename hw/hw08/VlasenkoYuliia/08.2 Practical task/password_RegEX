import re

def password_validation():
    password = input("Please enter your password:"'\n')
    if not re.findall("[a-z]", password):
        return "At least one lowercase letter is required"
    elif not re.findall("[A-Z]", password):
        return "At least one uppercase letter is required"
    elif not re.findall("\d", password):
        return "At least one number is required"
    elif not re.findall("[$#@]", password):
        return "At least one of the characters $, #, or @ is required"
    elif not re.findall("......16+", password):
        return "Your password must be between 6 and 16 characters long"
    return "Valid password"
print(password_validation())
