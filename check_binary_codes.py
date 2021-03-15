"""
Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k.
Return True if every binary code of length k is a substring of s. Otherwise, return False.

Solution: 
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        def _generate_combo():
            a, b = '0', int('1',2)
            yield a
            while True:
                a = bin(int(a,2) + b)[2:]
                yield a
        for i in _generate_combo():
            if len(i) > k:
                break
            elif i.zfill(k) not in s:
                return False   
        return True


solution = Solution()
result = solution.hasAllCodes("00110110", 2)

print(result)


""" x = 34
x = f'{x:05}'
print(x) """
