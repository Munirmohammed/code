from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_frequency = max(c.values())
        total_frequency = sum(freq for freq in c.values() if freq == max_frequency)
        
        return total_frequency