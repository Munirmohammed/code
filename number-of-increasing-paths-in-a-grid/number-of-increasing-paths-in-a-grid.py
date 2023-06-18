class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9+7
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = 0

        @lru_cache(maxsize = None)
        def dfs(i, j):
            ans = 0
            for dx, dy in directions:
                if (0 <= i + dx < m) and (0 <= j + dy < n) and (grid[i+dx][j+dy] > grid[i][j]):
                    ans += (1 + dfs(i+dx, j+dy))
            return ans
        
        for i in range(m):
            for j in range(n):
                res = (res + (dfs(i, j) % mod)) % mod
        
        return res+m*n
        