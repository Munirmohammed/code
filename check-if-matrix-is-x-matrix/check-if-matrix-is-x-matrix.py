class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if((i!=j and i+j!=n-1) and grid[i][j]!=0):
                    return 0
                elif((i==j or i+j==n-1) and grid[i][j]==0):
                    return 0
        return 1
