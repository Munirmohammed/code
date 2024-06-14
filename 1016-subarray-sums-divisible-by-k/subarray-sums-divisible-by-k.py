class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}  
        curr_sum = 0  
        count = 0  

        for num in nums:
            curr_sum += num  
            rem = curr_sum % k  
            if rem < 0:  
                rem += k
            count += prefix_sum.get(rem, 0)  
            prefix_sum[rem] = prefix_sum.get(rem, 0) + 1  

        return count