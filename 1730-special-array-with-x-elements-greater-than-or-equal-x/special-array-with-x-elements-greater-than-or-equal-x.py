class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= i and (i == len(nums) or nums[i] < i):
                return i
        return -1