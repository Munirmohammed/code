class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j,ans=0,len(nums)-1,0
        nums.sort()
        while i < j:
        
            temp = nums[i] + nums[j]
            if temp == k:
                ans+=1
                i+=1
                j-=1
            elif temp < k:
                i+=1
            else:
                j-=1
        return ans
        