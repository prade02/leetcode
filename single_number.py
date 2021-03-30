"""
Approach 1: sort list in place. iterate with step as 2. compare i and i+1 is at any point they are different, return i.
Approach 2: no sorting, but use of additional memory, dict. iterate through the list, if the num not present in dict key, add  num as key and value as 1
else increment the value with 1. once done, iterate through the dict return the key with value as 1
"""

def singleNumber_v1(nums):
    nums.sort()
    i = 0
    while i + 1 < len(nums):
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 2
    return nums[i]


def singleNumber_v2(nums):
    d = {}
    for num in nums:
        d[num] = d.setdefault(num, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k


x = [2,2,1]
print(singleNumber_v2(x))