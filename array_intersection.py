"""
Approach 1: iterate thought the list1 and check if the item is present in list 2, if yes call remove in list2 of that item to remove the first occurance of it.
also add the item to the result list. at the end for all the items in list1 if it is present is list2, that will be added in result list -> intersection of 
these arrays with exact occurance.

Approach 2: use Counter from collections. it gives a dict of keys as the items and value as the number of times item is present in the list.
use the counter 1 iterate through it, if the key is also present in counter 2, the min value of these 2 is the occurance of the item in the result list
"""
from collections import Counter
def intersect_v1(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2:
            nums2.remove(num)
            result.append(num)
    return result


def intersect_v2(nums1, nums2):
    result = []
    x = Counter(nums1)
    y = Counter(nums2)
    x, y = (x, y) if len(y) > len(x) else (y, x)
    for k in x:
        result += [k] * min(x[k], y[k])
    return result


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect_v2(nums1, nums2))