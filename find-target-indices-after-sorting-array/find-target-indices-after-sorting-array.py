class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums.sort()
        arr = []
        for i in range(n):
            if nums[i] == target:
                arr.append(i)
        return arr