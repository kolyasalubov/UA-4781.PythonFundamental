def max_number(num1: float, num2: float) -> float:
    """This function return the max number
    Input: number1 - float, number2 - float
    Output: float
    """
    if num1 > num2:
        print (num1)
    elif num2 > num1:
        print(num2)
    else: 
        print("The numbers are equal")

number1 = float(input("Print the number 1: "))
number2 = float(input("Print the number 2: "))
max_number(number1,number2)
