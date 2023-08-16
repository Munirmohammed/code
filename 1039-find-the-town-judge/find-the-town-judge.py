class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        degree = [0 for i in range(0,n+1)]
        for i,j in trust:
            degree[i] -= 1
            degree[j] += 1
        for i in degree:
            if i == n-1:
                return degree.index(i)
        return -1