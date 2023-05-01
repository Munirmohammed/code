class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        dp = [0] * len(nums)
        k = nums[-1] - nums[-2] 
        for i in range(len(nums) -3, -1,-1):
            if nums[i] + k == nums[i + 1] == nums[i + 2] - k: 
                dp[i] = dp[i + 1] + 1
            k = nums[i + 1] - nums[i]
        return sum(dp)