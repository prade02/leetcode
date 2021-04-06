"""
Approach 1: convert the string to a list which filters only alpnum. reverse the list and if both are same then return true
Approach 2: convert the string to a list which filters only alpnum. two pointer approach. i=0, j=n-1. compare both till i >=0. return flase if at any point i and j element are not 
equal, else if iteration is complete return true
Approach 3: dont create a list excluding other char. iterate through the list with 2 pointer approach. if ith or jth element is other char pass, if ith and jth element are
alnum, compare, if not same return false. if iteration completes return true
"""

def isPalindrome_v1(s):
    list_a = [c.lower() for c in s if c.isalnum()]
    if list_a == list_a[::-1]:
        return True
    return False


def isPalindrome_v2(s):
    list_a = [c for c in s if c.isalnum()]
    i = 0
    j = len(list_a) - 1
    while i < j:
        if list_a[i].lower() != list_a[j].lower():
            return False
        i += 1
        j -= 1
    return True


def isPalindrome_v3(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


x = 'A man, a plan, a canal: Panama'
print(isPalindrome_v3(x))