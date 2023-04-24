class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = 10001
        sm = [0] * n
        dp = [0] * n
        
        for num in nums:
            sm[num] += num
        
        dp[0] = 0
        dp[1] = sm[1]

        for i in range(2, n):
            dp[i] = max(dp[i-2] + sm[i], dp[i-1])
        
        return dp[n-1]