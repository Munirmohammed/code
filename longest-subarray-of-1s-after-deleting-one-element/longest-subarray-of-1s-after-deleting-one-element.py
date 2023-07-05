class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev=0
        count=0
        ls=[]
        visit=False
        for i in nums:
            if i==0:
                visit=True
                ls.append(prev+count)
                prev=count
                count=0
            if i==1:
                count+=1
        if not visit:
            count-=1
        ls.append(count+prev)
        return max(ls)