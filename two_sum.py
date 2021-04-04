"""
Approach 1: a + b = c, a - c = b, c is target, a and b is from the list, so for every a in the list search if b exists, if so a and b forms c(target)
iterate through the list, get a, in the inner iteration, start from i+1 - since sum of elements can not be same. so search for elements after i.
"""


def twoSum(nums, target):
    _len = len(nums)
    for i in range(_len):
        search_for = target - nums[i]
        for j in range(i+1, _len):
            if nums[j] == search_for:
                return [i, j]


x = [3,3]
print(twoSum(x, 6))
