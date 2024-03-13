class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if not (s1[0] == s2[0] == s3[0]):
            return -1
        k = 0
        for c1, c2, c3 in zip(s1, s2, s3):
            if not (c1 == c2 == c3): break
            k += 1 
        return len(s1) + len(s2) + len(s3) - k * 3