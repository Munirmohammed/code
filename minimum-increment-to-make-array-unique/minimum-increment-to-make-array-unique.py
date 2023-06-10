class Solution:
    def minIncrementForUnique(self, A):
        res=0
        originalSum=sum(A)
        A.sort()
        
        for i in range(1, len(A)):
            if A[i]<=A[i-1]:
                A[i]=A[i-1]+1
        return sum(A)-originalSum