class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        if n==1:
            return 1
        visited=[[0 for j in range(n)] for i in range(n)]
        q=deque()
        q.append([0,0,1])
        while q:
            i,j,t=q.popleft()
            visited[i][j]=1
            for row in range(-1,2):
                for col in range(-1,2):
                    r,c=i+row,j+col
                    if 0<=r<n and 0<=c<n and visited[r][c]==0 and grid[r][c]==0:
                        visited[r][c]=t+1
                        if r==n-1 and c==n-1:
                            return t+1
                        q.append([r,c,t+1])
        return -1