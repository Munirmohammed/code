class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [0, 0] + [1] * (n - 2)
        for i in range(2,int(sqrt(n)+1)):
            if nums[i]==1:
                for j in range(i*i,n,i):
                    nums[j]=0
        return sum(nums)