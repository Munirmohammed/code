class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        ans = 0

        for row in grid:
            d[tuple(row)] += 1

        for col in zip(*grid):
            ans += d[tuple(col)]

        return ans