class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper():
            memo = [0 for _ in range(len(nums))]
            memo[0] = nums[0]
            for i in range(1, len(nums)):
                incl = nums[i]+memo[i-2] if i-2 >=0 else nums[i]
                excl = memo[i-1]
                memo[i] = max(incl, excl)
            return memo[len(nums)-1]
        return helper()