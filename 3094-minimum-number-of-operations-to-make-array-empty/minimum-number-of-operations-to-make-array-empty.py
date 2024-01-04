class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        ans=0
        for x in nums:
            freq[x]+=1
        for _, f in freq.items():
            if f==1: return -1
            q, r= divmod(f,3)
            if r==0: rem=0
            else: rem=1
            ans+=q+rem
        return ans