class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sum(target) == sum(arr) and sum(t*t for t in target) == sum(a*a for a in arr)       