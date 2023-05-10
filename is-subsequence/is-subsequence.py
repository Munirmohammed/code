class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for m in t:
            if i==len(s):
                return True
            if s[i]==m:
                i+=1
        return i==len(s)