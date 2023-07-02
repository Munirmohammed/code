class Solution:
    def dp(self,i,lst,requests,n,dct):
        if i<0:
            if lst[:]==[0]*n:
                return 0
            return float("-infinity")
        if (i,tuple(lst)) in dct:
            return dct[(i,tuple(lst))]
        frm=requests[i][0]
        to=requests[i][1]
        lst[frm]-=1
        lst[to]+=1
        x=self.dp(i-1,lst,requests,n,dct)+1
        lst[frm]+=1
        lst[to]-=1
        y=self.dp(i-1,lst,requests,n,dct)
        dct[(i,tuple(lst))]=max(x,y)
        return max(x,y)


    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        lst=[0]*n
        m=len(requests)
        ans=self.dp(m-1,lst,requests,n,{})
        if ans==float("-infinity"):
            return -1
        return ans