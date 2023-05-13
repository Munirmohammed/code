class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m=len(mat)
        n=len(mat[0])
        if m*n != r*c:
            return mat
        flat=[]
        for i in mat:
            flat.extend(i)
    
        output=[]
        for i in range(r):
            output.append(flat[i*c:(i+1)*c])
        return output