class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        most_common_element, _ = c.most_common(1)[0] 
        return most_common_element

        