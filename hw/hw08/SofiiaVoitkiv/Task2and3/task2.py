import re
password = input("Create your password: ")

lower_case = re.search("[a-z]", password)
upper_case = re.search("[A-Z]", password)
numbers = re.search("[0-9]", password)
symbols = re.search("[$#@]", password)
min_len = len(password) >= 6
max_len = len(password) <= 16

if lower_case and upper_case and numbers and symbols and min_len and max_len:
    print("Your password accepted")
else:
    print("Try again")
