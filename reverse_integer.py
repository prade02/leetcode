"""
Approach 1: convert the int to str, reverse the str, convert the str to int. if int is < 0, strip the - before reversing, then concatenate - and convert to int
"""

def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x *= -1
    str_r = str(x)
    str_r = str_r[::-1]
    x = int(str_r)
    if negative:
        x *= -1
    if -2**31 < x < (2**31 - 1):
        return x
    return 0


x = 120
print(reverse(x))
