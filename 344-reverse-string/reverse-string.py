class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j=len(s)-1
        def rev(s,i,j):
            if i>=j:
                return
            s[i],s[j]=s[j],s[i]
            rev(s,i+1,j-1)
        rev(s,i,j)