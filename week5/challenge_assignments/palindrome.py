"""
Description: Check if a given string is a palindrome, i.e., it reads the same forward and backward.
Input Arguments:
s (str): The string to check.
"""

def is_palindrome(value): 
    value_reversed = ""
    
    # we can loop to reverse...
    size_of_value = len(value)
    for i in range(size_of_value):
        value_reversed += value[size_of_value-i-1]

    # ...or we can use fancier slicing like this
    value_reversed = value[::-1]

    return value == value_reversed
