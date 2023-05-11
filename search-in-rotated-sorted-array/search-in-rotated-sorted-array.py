class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i == target:
                return count
            count += 1
        return -1