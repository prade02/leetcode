"""
Approach 1: sort the list to bring the items closer - items with least common prefix will be closer. compare first 2 items and check how many char's are common.
the count should be the longest common prefix - iterate through the list and check if all the items has the same common prefix
"""

def longestCommonPrefix(strs):
    result = ''
    if len(strs) < 1:
        return result
    elif len(strs) < 2:
        return strs[0]
    # strs.sort()
    first = strs[0]
    second = strs[1]
    count = 0
    for i in range(1, len(first) + 1):
        if first[:i] == second[:i]:
            count += 1
        else:
            break
    if count == 0:
        return result
    result = first[:count]
    for item in strs:
        if item[:count] != result:
            # readjust the prefix
            count -= 1
            while count > 0: 
                if item[:count] == result[:count]:
                    result = result[:count]
                    break
                count -= 1
            else:
                return ''
    return result


x = ["flower","flow","flight"]
print(longestCommonPrefix(x))