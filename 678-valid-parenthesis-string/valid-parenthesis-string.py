class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        par_stack = []
        n = len(s)
        i = 0
        while i<n:
            if s[i]=='(':
                par_stack.append(i)
            elif s[i]=='*':
                star_stack.append(i)
            else:
                if par_stack:
                    par_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            i+=1
        print(star_stack)
        print(par_stack)
        while par_stack:
            if len(star_stack)==0:
                return False
            if par_stack[-1]>star_stack[-1]:
                return False
            par_stack.pop()
            star_stack.pop()
        return True

                    
                
        