def strStr_v1(haystack, needle):
    if needle == '':
        return 0
    elif needle in haystack:
        return haystack.index(needle) # use index, throws if the str is not found, hence membership has to be tested
    return -1

def strStr_v2(haystack, needle):
    if needle == '':
        return 0
    return haystack.find(needle) # use find - when str not found returns -1, so need to check for membership



h = 'hello'
n = 'sss'
print(strStr_v2(h,n))