"""
Approach 1: if len of 2 are not equal return false. else, convert the string to array and sort, if both the list are same
then it is an anagram

Approach 2: using counter. create counter object for both the strings and if both are equal, return true
"""
from collections import Counter

def isAnagram_v1(s, t):
    if len(s) != len(t):
        return False
    list1 = list(s)
    list2 = list(t)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


def isAnagram_v2(s, t):
    return Counter(s) == Counter(t)


x = 'anagram'
y = 'nagaram'
print(isAnagram_v2(x,y))