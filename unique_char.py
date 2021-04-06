"""
Approach 1: create a list out of string - list of char. use counter to get count of each items in the list - dict. in the dict see what key has value as 1 and return the index
of the item in the list, else if no key has value as 1, return -1

Approach 2: less memory more run time. iterate through the string, check count of each item, if any one has 1 return that items index
"""
from collections import Counter
def firstUniqChar_v1(s):
    item_counter = Counter(s)
    for k,v in item_counter.items():
        if v == 1:
            return s.index(k)
    return -1


def firstUniqChar_v2(s):
    for i,c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1

x = 'leetcode'
print(firstUniqChar_v2(x))
