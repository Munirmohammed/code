class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        if len(mat) == 2:
            return mat[0][0] + mat[1][1]
        sum = 0
        if len(mat) % 2 != 0:
            n = len(mat) / 2
            sum -= mat[int(n)][int(n)]
            print(sum)
        for k in range(len(mat)):
            sum += mat[k][k]
        for i in range(len(mat)):
            for j in range(len(mat)-1,-1,-1):
                sum += mat[i][j]
                print(mat[i][j],i,j)
                i+=1
            break
        return sum