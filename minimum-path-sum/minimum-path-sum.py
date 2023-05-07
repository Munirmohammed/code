class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        M, N = range(1,m),range(1,n)

        for i in N: grid[0][i] += grid[0][i - 1]              
                                                            
        for j in M: grid[j][0] += grid[j - 1][0]            

        for i, j in product(M,N):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])   

        return grid[m-1][n-1]                               