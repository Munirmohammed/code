class Solution:
    def numSquares(self, n: int) -> int:
        def backtrack(i, target, currLen, minLen):
            if target == 0:
                return min(minLen, currLen)
            
            if i < 1 or currLen >= minLen:
                return minLen

            if i**2 <= target:
                minLen = backtrack(i, target - i**2, currLen + 1, minLen)
      
            minLen = backtrack(i-1, target, currLen, minLen)
            return minLen

        return backtrack(int(math.sqrt(n)), n, 0, float('inf'))
      