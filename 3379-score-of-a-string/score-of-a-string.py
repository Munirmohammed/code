class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = ord(s[0])
        for i in range(1, len(s)):
            char = ord(s[i])
            score += abs(char-prev)
            prev=char
        return score