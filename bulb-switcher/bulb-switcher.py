class Solution:
    def bulbSwitch(self, n: int) -> int:
        count = 0
        i = 1
        while i*i <= n:
            count += 1
            i += 1
        return count