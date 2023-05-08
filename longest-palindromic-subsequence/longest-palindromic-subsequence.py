class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def lcs(i: int, j: int) -> int:
            if i >= len(s) or j < 0:
                return 0
            if s[i] == s[j]:
                return 1 + lcs(i + 1, j - 1)
            return max(lcs(i + 1, j), lcs(i, j - 1))

        return lcs(0, len(s) - 1)