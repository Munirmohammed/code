class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        for i in nums:
            if x != i:
                return x
            x += 1
        return x
