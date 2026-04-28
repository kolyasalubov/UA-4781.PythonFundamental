def char_counter(words):
    result = {}
    for lt in words:
        if lt in result:
            result[lt] += 1
        else:
            result[lt] = 1
    return result

word = input('Input word:')
print(char_counter(word))

            

