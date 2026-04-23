#Task3. Write a function that calculates the number of caharacters included in given string. 
# ( input: 'hello' output: {'h': 1, 'e': 1, 'l': 2, 'o': 1} )
def count_characters(input_string):
    """
    This function takes a string as input and returns a dictionary with the count of each character in the string.
    """
    char_count = {}
    for char in input_string:
        char_count.setdefault(char, 0)
        if char in char_count:
            char_count[char] += 1
    
    return char_count
# Verification of the function
if __name__ == "__main__":
    print(count_characters('hello'))