class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        for i in range(len(dp)):
            if int(sqrt(i)) == sqrt(i):
                dp[i] = 1
            else:
                for j in range(int(sqrt(i))+1):
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]