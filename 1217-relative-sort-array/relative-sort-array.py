class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * (max(arr1) + 1)
        for num in arr1:
            count[num] += 1
        
        res = []
        for num in arr2:
            res.extend([num] * count[num])
            count[num] = 0
        
        for i, num in enumerate(count):
            if num > 0:
                res.extend([i] * num)
        
        return res