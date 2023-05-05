class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        cum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cum[i][j] = mat[i][j]
                if i > 0:
                    cum[i][j] += cum[i-1][j]
                if j > 0:
                    cum[i][j] += cum[i][j-1]
                if i > 0 and j > 0:
                    cum[i][j] -= cum[i-1][j-1]
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(i-k, 0), max(j-k, 0)
                r2, c2 = min(i+k, m-1), min(j+k, n-1)
                answer[i][j] = cum[r2][c2]
                if r1 > 0:
                    answer[i][j] -= cum[r1-1][c2]
                if c1 > 0:
                    answer[i][j] -= cum[r2][c1-1]
                if r1 > 0 and c1 > 0:
                    answer[i][j] += cum[r1-1][c1-1]
        return answer