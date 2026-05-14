# def num_characters(string):
#     """Calculate the number of characters in a string."""
#     counters = {} 
#     for i in string:
#         if i not in counters:
#             counters[i] = 1
#         else:
#             counters[i] += 1
#     return counters
# user_input = input("Enter a string: ")
# print(f"Output: {num_characters(user_input)}")

def bool_to_word(boolean):
    return "Yes" if boolean else "No"