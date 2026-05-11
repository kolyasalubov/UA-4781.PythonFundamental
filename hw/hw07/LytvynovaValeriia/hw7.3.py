def calculating_characters (string: str):
    """
    Docstring for calculating_characters
    This function calculating the characters in a string
    Input: string - str
    """
    result = {}
    
    for item in string:
        if item == ' ':
            continue
        elif item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    print(result)


calculating_characters(input("Write your word: "))