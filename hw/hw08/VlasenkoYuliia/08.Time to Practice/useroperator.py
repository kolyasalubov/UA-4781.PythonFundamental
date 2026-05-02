from calculator import addition, substraction, multiplication, division
print("*"*20)
print("Math operators")
print("What operation do you want to perform?")
print("Addition +, Substraction -, Multiplication *, Division / " )

while True:
    operator = input("Please enter your operator or q to Exit: ")
    match operator:
        case "q":
            print("Exit")
            break

        case "+":
            a = float(input("Please enter numb1: " '\n'))
            b = float(input("Please enter numb2: " '\n'))
            print(f"The result of addition is {addition(a, b)}")
        case "-": 
            a = float(input("Please enter numb1: " '\n'))
            b = float(input("Please enter numb2: " '\n'))
            print(f"The result of substraction is {substraction(a, b)}")
        case "*":
            a = float(input("Please enter numb1: " '\n'))
            b = float(input("Please enter numb2: " '\n'))
            print(f"The result of multiplication is {multiplication(a, b)}")
        case "/":    
            a = float(input("Please enter numb1: " '\n'))
            b = float(input("Please enter numb2: " '\n'))
            print(f"The result of division is {division(a, b)}")
        case _:
            print("Please, enter one of operators")
    