class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            result = 1
            while n > 0:
                result *= n
                n -= 1
            return result
        
        nums = list(range(1, n+1))
        k -= 1
        result = []
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i-1]*i
        for i in range(n-1, -1, -1):
            index = k // dp[i]
            result.append(str(nums[index]))
            nums.pop(index)
            k %= dp[i]
        return ''.join(result)