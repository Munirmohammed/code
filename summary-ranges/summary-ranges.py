class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:return []
        ans,i=[],0
        st=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if st==nums[i-1]:
                    ans.append(str(st))
                else:
                    ans.append(str(st)+"->"+str(nums[i-1]))
                st=nums[i]
        if st==nums[-1]:
            ans.append(str(st))
        else:
            ans.append(str(st)+"->"+str(nums[len(nums)-1]))
        return ans