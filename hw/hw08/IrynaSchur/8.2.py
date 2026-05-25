password = input("Print your passwod: ")

is_valid = True

# Length check
if not (6 <= len(password) <= 16):
    is_valid = False

# Conditions
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "$#@" for c in password)

if not (has_lower and has_upper and has_digit and has_special):
    is_valid = False

if is_valid:
    print("Valid password")
else:
    print("Invalid password")