"""
Approach 1: update list in place. run time optimised. iterate through list, pop out 0 and have counter to count no of times 0 is popped. once iteration is done, add the 0's at end
Approach 2: update list in place. memory optimised. iterate though list for len of the list. if item is 0, remove and append - list will be iterated in fixed length
"""

def moveZeroes_v1(nums):
    count = 0  
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
        else:
            i += 1
    nums.extend([0] * count)


def moveZeroes_v2(nums):
    for num in nums:
        if num == 0:
            nums.remove(0) # this takes time
            nums.append(0)


x = [0]
moveZeroes_v2(x)
print(x)