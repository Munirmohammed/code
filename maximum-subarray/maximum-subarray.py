class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        arr = []
        for i in range(len(nums)):
            sum = max(nums[i] , sum +nums[i] )
            arr.append(sum)
        arr.sort()
        print(arr)
        return arr[-1]