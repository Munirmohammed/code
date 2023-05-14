class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j)
                if matrix[i][0] > target:
                    break
                if matrix[i][j] == target:
                    return True
        return False