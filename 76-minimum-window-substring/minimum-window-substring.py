class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, tn= len(s), len(t)
        left=0
        mp=[0]*64
        tmp=[0]*64

        for c in t:
            idx=ord(c)& 63
            tmp[idx]+=1
        count=0
        minLength=2**31
        minLeft=0

        for right, c in enumerate(s):
            idx=ord(c)& 63
            if tmp[idx]==0: continue
            mp[idx]+=1
            if mp[idx]<=tmp[idx]: count+=1
            if count==tn:
                while tmp[ll:=(63& ord(s[left]))]==0 or mp[ll]>tmp[ll]:
                    if mp[ll]!=0: mp[ll]-=1
                    left+=1
                if right-left+1<minLength:
                    minLength=right-left+1
                    minLeft=left
        if minLength==2**31: return ""
        return str(s[minLeft:minLeft+minLength])
        