class Solution:
    def longestPalindrome(self, s: str) -> str:

        N, l, r = len(s), 0, 1
        
        for i in range(N):
            for a, b in (i, i), (i, i+1):
                while 0 <= a and b < N and s[a] == s[b]: a, b = a-1, b+1
                if b-a > r-l: l, r = a+1, b
        
        return s[l:r]