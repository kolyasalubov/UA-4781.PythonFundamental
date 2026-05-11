def count_chars(word):
    '''
    Calculate the number of each character in the word.
    '''
    result = dict()
    for char in word:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result
 
word = input("Put the word: ")
print(count_chars(word))


