class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def isVowel(c):
            return (0x208222>>(c&0x1f))&1
        n=len(s)//2
        f=0
        for i in range(n):
            f+=(isVowel(ord(s[i]))-isVowel(ord(s[n+i])))
        return f==0