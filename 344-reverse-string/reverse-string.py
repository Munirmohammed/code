class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)//2
        for i in range(n):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        