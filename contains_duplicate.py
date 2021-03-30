"""
Approach 1: time optimised - create a set by passing the list in the constructor. if len of set and list are same, then no duplicates else it has duplicates
Approach 2: iterate through the list, for each item check if count of that item in the list is more than 1, if yes, return true
Aproach 3: similar to approach 1, but dont create set with all items, create an empty set, add items in iteration, if an item found already in set, return true
else false
Approach 4: memory optimised - iterate through the list after sorting in place until last but one, if i and i+1 are same return true, else false
"""

def containsDuplicate_v1(nums):
    s = set(nums)
    if len(s) == len(nums):
        return False
    return True


# takes more time
def containsDuplicate_v2(nums):
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False


def containsDuplicate_v3(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False


def containsDuplicate_v4(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False
