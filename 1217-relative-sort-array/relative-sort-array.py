class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {num: 0 for num in arr1}
        for num in arr1:
            count[num] += 1
        
        res = []
        for num in arr2:
            res.extend([num] * count[num])
            del count[num]
        
        remaining = sorted(count.keys())
        for num in remaining:
            res.extend([num] * count[num])
        
        return res