class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [] if len(original) != m*n else [original[i:i+n] for i in range(0, m*n, n)]