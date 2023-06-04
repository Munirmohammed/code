class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr, left  = [], 0
        for i in range(len(nums)):
            bisect.insort(arr, nums[i])
            if arr[-1] - arr[0] > limit:
                arr.pop(bisect.bisect(arr, nums[left])-1)
                left += 1
        return i - left + 1

