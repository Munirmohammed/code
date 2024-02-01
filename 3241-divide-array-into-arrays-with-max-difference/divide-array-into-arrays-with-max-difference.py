class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        ans = []
        for i in range(0,l,3):
            if nums[i+2]-nums[i] <= k:
                ans.append([nums[i],nums[i+1],nums[i+2]])
            else:
                return []
        return ans