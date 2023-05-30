class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x = {'+', '-', '*', '/'}
        arr = []
        
        for i in tokens:
            if i not in x:
                arr.append(int(i))
            if i in x:
                m = arr.pop()
                n = arr.pop()
                if i == '+':
                    sm = n + m
                    arr.append(sm)
                elif i == '-':
                    df = n - m
                    arr.append(df)
                elif i == '*':
                    pr = n * m
                    arr.append(pr)
                elif i == '/':
                    dv = int(n / m)
                    arr.append(dv)
        
        return arr[-1]
