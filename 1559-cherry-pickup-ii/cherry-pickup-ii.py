class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp_prev = defaultdict(lambda: -float("inf"))
        dp_prev[(0, n - 1)] = grid[0][0] + grid[0][n - 1]
        for row in grid[1:]:
            dp = defaultdict(lambda: -float("inf"))
            for i in range(n):
                for j in range(i, n):
                    dp[(i, j)] = (
                        row[i] + row[j] if i != j else row[i]
                    ) + max(
                        dp_prev[(i + di, j + dj)]
                        for di in {-1, 0, 1}
                        for dj in {-1, 0, 1}
                    )
            dp_prev = dp
        return max(dp.values())