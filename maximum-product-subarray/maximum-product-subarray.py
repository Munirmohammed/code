class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out=max(nums)
        cmax=cmin=1
        for n in nums:
            temp=cmax*n
            cmax=max(cmin*n,cmax*n,n)
            cmin=min(temp,cmin*n ,n)
            out=max(out,cmax)
        return out

        