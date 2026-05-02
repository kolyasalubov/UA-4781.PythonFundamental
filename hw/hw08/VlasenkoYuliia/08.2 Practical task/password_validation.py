def password_validation():
    password = input("Please enter your password:"'\n')
    sp_chart_list = ["$", "#", "@"]
    if len(password)<6 or len(password)>16:
        return "Your password must be between 6 and 16 characters long"
    elif any([val.isupper() for val in password]) == False:
        return "At least one uppercase letter is required"
    elif any([val.islower() for val in password]) == False:
        return "At least one lowercase letter is required"
    elif any([val.isdigit() for val in password]) == False:
        return "At least one number is required"
    elif any([ bool(val) for val in password if val in sp_chart_list ]) == False:
        return "At least one of the characters $, #, or @ is required"
    return "Valid password"

print(password_validation())


