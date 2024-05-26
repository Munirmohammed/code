class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        dp[0][0][0] = 1
        
        for i in range(1, n+1):
            for j in range(2):
                for k in range(3):
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    if j > 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-1][j-1][k]) % MOD
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % MOD
        
        res = 0
        for j in range(2):
            for k in range(3):
                res = (res + dp[n][j][k]) % MOD
        return res