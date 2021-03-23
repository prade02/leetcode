"""
Approach 1: iterate through list and remove items which are of duplicates using for loop
loop through the list in the reverse order - this way when we are updating/removing a list when iterating the items processed are in the right side and even 
if the shift to one position to left, this will not affect items on the left side of the pointer.

Approach 2: iterate using while loop in same order
in the iteration compare current element with next element, if same pop the current item and dont increment the index. else dont pop and increment the index.

Approach 3: iterate but dont remove items in the array instead have a counter to count the unique items. if the problem is just to count the unique items, this
would fit better since it is faster as list modification is not altered.

Approach 4: same as #3 but we are going to change list elements. if l = [1,2,2,3] after processing it will be [1,2,3,3] - a pointer to track the items upto 
which unique elements are calculated.
    i and j as 0, iterate the list, if i and i+1 are diff then increment j, in l[j] put the i+1 item, when items are same, dont do anything. so for same items
    j will not increment, once a diff item is found in i, increment j put that element in the j i.e., l[j] = l[i]

Approach 5: its a cheat way - create a set by inputting the list in the constructor.
"""

def remove_duplicates(nums):    
    previous_value = None
    for index in range(len(nums) - 1, -1, -1):
        if nums[index] == previous_value:
            nums.pop(index + 1)
        previous_value = nums[index]
    return len(nums)


def remove_duplicates_v2(nums):   
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


def remove_duplicates_v3(nums):    
    j = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            j += 1
    return j


def remove_duplicates_v4(nums):    
    j = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i + 1]
            j += 1
    return j


def remove_duplicates_v5(nums):    
    s = set(nums)
    return len(s)

x = [1,2,2,3,3,4,5,7,7,]
print(remove_duplicates_v5(x))
