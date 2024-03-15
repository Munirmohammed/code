class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         output = [0]*n
         output[0] = 1
         for i in range(1, n):
            output[i] = nums[i-1] * output[i-1]

         right = 1
         for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

         return output