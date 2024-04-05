class Solution:
    def makeGood(self, s: str) -> str:
        res = [s[0]]
        letter_diff = ord("a") - ord("A")
        for i in range(1, len(s)):
            if not res or abs(ord(s[i]) - ord(res[-1])) != letter_diff:
                res.append(s[i])
            else:
                res.pop()  
        return "".join(res)