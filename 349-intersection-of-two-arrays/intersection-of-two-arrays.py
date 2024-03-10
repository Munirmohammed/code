class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = set()
        s = set(nums1)
        for num in nums2:
            if num in s:
                k.add(num)
        return list(k)

        