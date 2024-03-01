class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return '1' * ((ones:=s.count('1')) - 1) + '0' * (len(s)-ones) + '1'