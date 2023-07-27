class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        def check(n,mid):
            return sum(mid if i>mid else i for i in b)/n>=mid
        i,j=0,10**20
        while i<j:
            mid=(i+j)//2
            if check(n,mid):
                i=mid+1
            else:
                j=mid
        return i-1