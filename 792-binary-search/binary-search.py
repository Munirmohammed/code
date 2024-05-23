class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return binsearch(start, mid-1)
            else:
                return binsearch(mid+1, end)
        return binsearch(0, len(nums)-1)        