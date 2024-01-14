class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1=len(word1)
        n2=len(word2)
        if n1!=n2:
            return False
        cnt1=Counter(word1)
        cnt2=Counter(word2)
        lst1=list(cnt1.values())
        lst2=list(cnt2.values())
        for i in range(26):
            if (cnt1[chr(ord('a')+i)]==0 and cnt2[chr(ord('a')+i)]!=0) or (cnt2[chr(ord('a')+i)]==0 and cnt1[chr(ord('a')+i)]!=0):
                return False
        lst1.sort()
        lst2.sort()
        return lst1[:]==lst2[:]
        