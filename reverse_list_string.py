"""
Approach 1: two pointer approach. i and j are pointers. i starts with 0 and j starts with last index. iterate through the list, and swap item at i and j.
the iteration will break when i >= j.
"""

def reverseString(s):
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


x = ["H","a","n","n","a","h"]
reverseString(x)
print(x)