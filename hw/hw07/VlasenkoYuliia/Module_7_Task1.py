
def largest_number(numb1, numb2):
    """This function returns
       the largest number of 
       two numbers"""
    if numb1 > numb2:
        return f"the largest of {numb1} and {numb2} is {numb1}"
    return f"the largest of {numb1} and {numb2} is {numb2}"

print(largest_number(5, 2))
print(largest_number(5, 10))