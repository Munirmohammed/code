class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = sorted(c,key=lambda x:c[x],reverse=True)
        return c[:k]