class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def F(i,j,step):
            if step>maxMove:
                return 0
            if i<0 or i>=n or j<0 or j>=m:
                if step<=maxMove:
                    return 1
                return 0
            if dp[i][j][step]!=-1:
                return dp[i][j][step]
            left=F(i,j-1,step+1)
            right=F(i,j+1,step+1)
            down=F(i+1,j,step+1)
            up=F(i-1,j,step+1)
            dp[i][j][step]=left+right+up+down
            return (left+right+down+up)
        dp=[[[-1 for _ in range(maxMove+1)] for _ in range(m+1)] for _ in range(n+1)]
        return F(startRow,startColumn,0)%((10**9)+7)