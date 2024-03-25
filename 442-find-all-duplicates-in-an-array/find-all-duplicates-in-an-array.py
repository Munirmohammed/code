class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts: Dict[int, int] = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        duplicates: List[int] = []
        for num, count in counts.items():
            if count > 1:
                duplicates.append(num)
        
        return duplicates