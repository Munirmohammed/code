class Solution:
    def rob(self, nums: List[int]) -> int:
        def house(nums):
            rob1,rob2=0,0
            for num in nums:
                temp=max(num+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(house(nums[1:]),house(nums[:-1]),nums[0])