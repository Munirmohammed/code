class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pr = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            pr = pr * nums[i]
        if pr > 0:
            return 1
        else:
            return -1