class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        maxi = nums[0]
        currMin = nums[0]
        mini = nums[0]
        for num in nums[1:]:
            currMax = max(num, currMax + num)
            maxi = max(currMax, maxi)
            currMin = min(num, currMin + num)
            mini = min(currMin, mini)
        if sum(nums) == mini:    
            return maxi
        return max(maxi, sum(nums) - mini)