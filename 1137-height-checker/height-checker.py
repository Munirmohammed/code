class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(heights[i] != expected[i] for i in range(len(heights)))