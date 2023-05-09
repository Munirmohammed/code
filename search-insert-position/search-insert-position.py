class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        nums.append(target)
        nums.sort()
        for j in range(len(nums)):
            if nums[j] == target:
                return j