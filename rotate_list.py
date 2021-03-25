"""
Approach 1: use additional memory
k is the number of steps to rotate. if k > len, do modulus of k % len is new k. split the main list into 2. 
first list starts from k and to last. second list start from 0 and goes upto k but not including k.
concatenate first and second list gives final list. 

Approach 2: no additional memory - update list in place
k is the number of steps to rotate. shift one item at a time. iterate through the list, have a variable to hold the original value in the destination position
before shifting and shift to right. keep shifting 
note - this takes time to execute if array and k length increases
"""

def rotate_v1(nums, k):
    _len = len(nums)
    if k >= _len:
        k = k % _len
        if k == 0:
            return
    l1 = nums[-k:]
    l2 = nums[:-k]
    nums[:] = l1 + l2


def rotate_v2(nums, k):
    if len(nums) == k:
        return
    for i in range(k):
        x = None
        y = nums[-1]
        for j in range(len(nums) - 1):
            if x == None:
                x = nums[j + 1]
                nums[j + 1] = nums[j]
            else:
                nums[j + 1], x = x, nums[j + 1]
        nums[0] = y
    return

# did not work
def rotate_v3(nums, k):
    _len = len(nums)
    if k >= _len:
        k = k % _len
        if k == 0:
            return
    x = nums[0]
    i = 0
    while True:
        nums[(i + k) % _len], x = x, nums[(i + k) % _len]
        i = (i + k) % _len   
        if (_len % 2 == 0 and k % 2 == 0):
            if i == 0:
                i = _len - 1
                x = nums[i]
            elif i == _len - 1:
                break
        elif _len % k == 0:
            if i == 0:
                i = 1
                x = nums[i]
            elif i == 1:
                break
        elif i == 0:
            break
    return


# x = [1,2,3,4,5,6,7]


x = [1,2,3,4,5,6]
k = 3
rotate_v1(x, k)
print(x)

