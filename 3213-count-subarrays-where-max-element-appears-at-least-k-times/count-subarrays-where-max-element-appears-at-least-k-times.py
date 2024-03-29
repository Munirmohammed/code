class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        result = start = max_count_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_val:
                max_count_in_window += 1
            while max_count_in_window == k:
                if nums[start] == max_val:
                    max_count_in_window -= 1
                start += 1
            result += start
        return result