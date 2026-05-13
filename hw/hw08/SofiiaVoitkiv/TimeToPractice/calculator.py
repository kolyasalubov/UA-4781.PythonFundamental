import calc_func
import sys

selection = input("Select an operation (+, -, *, /): ")
if selection not in ["+", "-", "*", "/"]:
    print("You chose unavaliable operation")
else:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    if selection == "+":
        print(calc_func.add_numbers(num1, num2))
    elif selection == "-":
        print(calc_func.sub_numbers(num1, num2))
    elif selection == "*":
        print(calc_func.mult_numbers(num1, num2))
    elif selection == "/":
       print(calc_func.div_numbers(num1, num2))

