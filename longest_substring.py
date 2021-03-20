"""
Approach 1: iterate through the loop once
create a dict to hold unique substring with key as length of the substring
in the iteration initialise a list, add each char if not already available in list
    when a char is already in the list, add the contents to the dict and slice the list and get char after the duplicate and add current item to the list
"""

def longest(s):
    u = {}
    l = []
    for char in s:
        if char in l:
            ss = ''.join(l)
            u[len(ss)] = (ss)
            l = l[l.index(char)+1:]
        l.append(char)
    if len(l) > 0:
        ss = ''.join(l)
        u[len(ss)] = (ss)
        l.clear()
    return 0 if len(u) == 0 else max(u)


s = "dvdf"
print(longest(s))