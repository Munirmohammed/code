class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        # at this point xor_all contains the only number that appears odd times
    
        single = xor_all & ~(xor_all-1)  # set all but the least significant rightmost bit of xor_all to 0
                
        diff = 0
        for num in nums:
            if num & single:
                diff ^= num
        
        return [diff, xor_all^diff]