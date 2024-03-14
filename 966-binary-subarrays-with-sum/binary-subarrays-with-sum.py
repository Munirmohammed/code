class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        left1, left2 = 0, 0
        sum1, sum2 = 0, 0
        
        for right in range(len(nums)):
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            
            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            
            count += left2 - left1
        
        return count
