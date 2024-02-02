class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num.rstrip('02468')