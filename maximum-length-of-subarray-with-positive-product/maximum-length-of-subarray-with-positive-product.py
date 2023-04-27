class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = neg = pos = 0
        for x in nums:
            if x > 0:
                if neg > 0:
                    neg += 1
                pos += 1
            elif x < 0:
                neg, pos = pos+1, (neg+1 if neg else 0)
            else:
                neg = pos = 0
            ans = max(ans, pos)
        return ans
            
               