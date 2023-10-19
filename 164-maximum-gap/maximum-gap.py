class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        if len(nums) < 2:
            return 0
        for i in range(1,len(nums)):
            n = max(n, nums[i] - nums[i-1])
        
        return n