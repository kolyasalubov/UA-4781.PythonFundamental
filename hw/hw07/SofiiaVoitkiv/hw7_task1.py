def largest_num1(a, b):
    '''
    Returns the largest of two numbers.
    Args: a - first number
          b - second number
    Output: the largest number
    '''
    return max(a, b)

print(largest_num1(2, 3))
print(largest_num1(5, 9))
print(largest_num1(5555, 9))

print("-" * 10)
#####################################

def largest_num2(c, d):
    '''
    Returns the largest of two numbers.
    Args: a - first number
          b - second number
    Output: the largest number
    '''
    if c > d:
        return c
    else:
        return d
    
print(largest_num2(2, 3))
print(largest_num2(5, 9))
print(largest_num2(5555, 9))
