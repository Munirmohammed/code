class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        # Initialize counts for each type of subsequence
        count0, count1, count2 = 0, 0, 0
        
        # Traverse nums and update counts
        for num in nums:
            if num == 0:
                count0 = (count0 * 2 + 1) % mod
            elif num == 1:
                count1 = (count1 * 2 + count0) % mod
            else:
                count2 = (count2 * 2 + count1) % mod
        
        # The number of special subsequences formed is count2
        return count2
