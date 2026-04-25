a = int(input("num1: "))
b = int(input("num2: "))

def lrg_number(num1, num2):
    """Returns the larger number of two numbers."""
    if num1 > num2:
        return num1 
    else:
        return num2

print('The largest number its:',lrg_number(a, b))         
    