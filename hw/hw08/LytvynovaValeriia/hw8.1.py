import re

password = input("Print your passwod: ")

if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$", password):
    print("Correct password")
else:
    print("Incorect password:\n" \
    "Need to be: \n" \
    "At least 1 lowercase letter\n" \
    "At least 1 uppercase letter\n" \
    "At least 1 digit\n" \
    "At least 1 characters $#@\n" \
    "Minimum 6 and maximum 16 characters")


