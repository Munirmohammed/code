class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        prefix_sum = {0: -1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder in prefix_sum:
                if i - prefix_sum[remainder] >= 2:
                    return True
            else:
                prefix_sum[remainder] = i
        return False