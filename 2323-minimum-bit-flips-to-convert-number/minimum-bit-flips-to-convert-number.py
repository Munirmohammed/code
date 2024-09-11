class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_value = start ^ goal
        return bin(xor_value).count('1')
        