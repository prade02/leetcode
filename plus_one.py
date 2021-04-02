"""
Approach 1: two steps. first - create an integer out of given array. use join and use str() to convert each digit to string to join items. next convert the
str to int, increment to 1. second - create an int array with the integer. use list expression to iterate and pust each int() items into list
"""

def plusOne(digits):
    string_repr = ''.join(str(d) for d in digits)
    integer_repr = int(string_repr)
    integer_repr += 1
    string_repr = str(integer_repr)
    result = [int(s) for s in string_repr]
    return result


x = [0]
print(plusOne(x))