class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        d = {')':'(','}':'{',']':'['}
        for i in range(len(s)):
            if s[i] == "(" or  s[i] ==  "["  or s[i] ==  "{":
                sta.append(s[i])
              
            else:
                if sta:
                    a = sta.pop()
                else:
                    return False
              
                if a != d[s[i]]:
                    
                    return False
        return  not sta
                
                    