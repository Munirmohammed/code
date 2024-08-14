class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        
        def countPairs(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if countPairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left