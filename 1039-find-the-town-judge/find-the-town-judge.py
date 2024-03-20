class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = [0] * (n + 1)
        for a, b in trust:
            trust_counts[a] -= 1
            trust_counts[b] += 1
        for i in range(1, n + 1):
            if trust_counts[i] == n - 1:
                return i
        return -1