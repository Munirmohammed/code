class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        seen: Set[int] = set()

        for num in nums:
            if num in seen:
                result.append(num)
            seen.add(num)

        return result