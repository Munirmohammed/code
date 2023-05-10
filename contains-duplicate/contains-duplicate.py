class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            print(nums[i-1],nums[i])
            if nums[i-1] == nums[i]:
                return True
        return False