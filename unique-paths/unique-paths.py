class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        L_n=[0]
        for t in range(n-1):
            L_n.append(1)
        
        for i in range(m-1):
            L_o=L_n
            L_n=[1]
            for j in range(1,n):
                L_n.append(L_n[j-1]+L_o[j])
        return L_n[-1]
                