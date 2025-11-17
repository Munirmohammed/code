class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = False
        x = 0
        for i, num in enumerate(nums):
            if num == 1:
                if prev_one and x < k:
                    return False
                prev_one = True
                x = 0
            else:
                x += 1
        return True