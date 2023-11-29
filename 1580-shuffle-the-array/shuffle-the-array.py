class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        half_index = len(nums) // 2
        for i in range(len(nums) // 2):
            arr.append(nums[i])
            arr.append(nums[i + half_index])
        return arr
            