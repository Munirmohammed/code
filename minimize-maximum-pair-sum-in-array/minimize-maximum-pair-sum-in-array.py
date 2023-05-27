class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        list2=[]
        left,right=0,len(nums)-1
        while left<right:
            list2.append(nums[left]+nums[right])
            left+=1
            right-=1
        return max(list2)