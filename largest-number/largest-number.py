class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string=""
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        while len(nums)>0:
            largest=nums[0]
            index=0
            for i in range(len(nums)):
                if (nums[i]+largest)>(largest+nums[i]):
                    largest=nums[i]
                    index=i
            string+=largest
            nums.pop(index)
        if string[0]=='0':
            return "0"
        return string