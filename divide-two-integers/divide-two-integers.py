class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            return float('inf')
        
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            res += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)
        
        if negative:
            res = -res
        return min(max(-2147483648, res), 2147483647)