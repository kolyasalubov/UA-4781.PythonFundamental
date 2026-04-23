# Task1. Write a function that returns the largest number of two numbers(use DocString documentation strings in the function).

def largest_number(num1, num2):
    """
    This function takes two numbers as input and returns the largest of the two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2
# Verification of the function
if __name__ == "__main__":
    print(largest_number.__doc__)
    print("Largest number is:", largest_number(1, 2))