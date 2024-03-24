class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_table = {}
        
        for num in nums:
            if num in hash_table:
                return num
            else:
                hash_table[num] = 1
        
        return 0  # This will never be reached because the loop above will return the duplicate number if it exists
                  