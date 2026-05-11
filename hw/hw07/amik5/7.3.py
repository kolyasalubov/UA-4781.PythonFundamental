from collections import Counter

def count_characters(text):
    return dict(Counter(text))
print (count_characters("hello"))
