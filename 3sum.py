"""
find all unique triplets which sums to '0'. 

first version uses left and right pointers with sorting. iterate through the sorted array, fix the inital left pointer as i + 1 and right pointer as n - 1.
if sum of ith + lth+ rth elements are 0, then a match is found. if sum is < 0, increment the left pointer or if sum is > 0, decrement the right pointer - untill l < r
since the array is sorted, if sum is < 0, it means the left pointer which is smaller value is not enough to up the count to 0.
    if sum is > 0, means right pointer is much higher and we might need to reduce the upper limit.
additional: 
    if ith element is > 0, all elememts after here are positive and can not sum to 0, no need to proceed. 0 is not checked since if 3 0's are in row they are valid combinations
    when incrementing left or decrementing right, check if the next value is same as previous. in this case, the result is going to be the same so, move pointer to next unique one

second version iterates through the array with no sorting, pick ith and jth element. sum of these two with mutiply with -1 gives the 3rd element needed => this is the core.
c = -(i + j) 
first loop iterates from 0 to n-1. second runs through 1 to n. first iteration stores jth element is a set. on the second iteration check if 1 and 3 gives 2 which is stored in set
if it matches, then ith, jth, the element from set makes upto 0. else, add the jth element is set and move on.
"""
def find_3_sum(arr):
    arr.sort()
    n = len(arr)
    result = set()
    for i, a in enumerate(arr):
        if a > 0:
            break
        l = i + 1
        r = n - 1

        while l < r:
            f = arr[l]
            s = arr[r]
            sum = a + f + s
            if sum == 0:
                result.add((a, f, s))
                l += 1
                while l + 1 <= r and f == arr[l]: l += 1
            elif sum < 0:
                l += 1
                while l + 1 <= r and f == arr[l]: l += 1
            else:
                r -= 1
                while r - 1 >= l and s == arr[r]: r -= 1
    return result


def find_3_sum_v2(arr):
    n = len(arr)
    result = set()
    for i in range(n - 1):
        s = set()
        for j in range(i+1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                result.add((arr[i], arr[j], x))
            else:
                s.add(arr[j])
    return result


def find_3_sum_v3(arr):
    n = len(arr)
    result = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.add((arr[i], arr[j], arr[k]))
    return result

l = [-2,-2,-2,2,2,2,0,0,0]
print(find_3_sum(l))
print(find_3_sum_v2(l))
print(find_3_sum_v3(l))
            
