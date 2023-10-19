class Solution:
    def minimumRefill(self, plants: List[int], ca: int, cb: int) -> int:
        a,b=0,len(plants)-1
        alice,bob=ca,cb
        res=0
        while a<=b:
            if a==b:
                if alice>=bob:
                    if alice<plants[a]:
                        res+=1
                    return res
                else:
                    if bob<plants[b]:
                        res+=1
                    return res
            if plants[a]>alice:
                alice=ca
                res+=1
            if plants[b]>bob:
                bob=cb
                res+=1
            alice-=plants[a]
            bob-=plants[b]
            a+=1
            b-=1
        return res