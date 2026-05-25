def max_num(num1, num2):
    '''
    Returns the largest of two numbers.
    num1 (int): The first number.
    num2 (int): The second number.
    '''
    if num1 > num2:
        return num1
    return num2

number1 = (input("Print the number 1: "))
number2 = (input("Print the number 2: "))

if number1.isdigit() and number2.isdigit():
    number1 = int(number1)
    number2 = int(number2)
    print(f"The largest number is: {max_num(number1, number2)}")
else:
    print("Error: Please enter only positive integers.")