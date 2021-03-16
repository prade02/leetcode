"""
initialize all items to have one value at start.
sort the array and start from least.
formula:    value(i) = value(i) + (value(left) * value(right))
"""
class Solution:
    def numFactoredBinaryTrees(self, data) -> int:
        MOD = 10 ** 9 + 7
        data.sort()
        dp = [1] * len(data)
        index = {v: i for i, v in enumerate(data)}
        for current in data:
            for num1 in data:
                if num1 == current:
                    continue
                if current % num1 == 0:
                    num2 = current // num1
                    if num2 in data:
                        dp[index[current]] = dp[index[current]] + (dp[index[num1]] * dp[index[num2]])
        return sum(dp) % MOD
    
solution = Solution()
print(solution.numFactoredBinaryTrees([2,3,5,15,45,90]))
