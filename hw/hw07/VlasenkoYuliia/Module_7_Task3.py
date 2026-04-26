
def numb_characters(st):
    """ This function calculates 
    the number of characters included 
    in given string """
    d = {val: st.count(val) for val in set(st)}
    print(d)
numb_characters("hello")
    
