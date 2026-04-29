def function_list(text):
    new_dict={}
    for item in text:
        if item in new_dict :
            new_dict[item] +=1
        else :
            new_dict[item] = 1
    return new_dict
    
print(function_list("hello"))