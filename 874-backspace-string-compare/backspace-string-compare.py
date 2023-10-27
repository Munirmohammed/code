class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack2 = []
        for i in range(len(s)):
            if s[i] != '#':
                stack.append(s[i])
            if s[i] == '#':
                if stack:
                    stack.pop()
        for j in range(len(t)):
            if t[j] != '#':
                stack2.append(t[j])
            if t[j] == '#':
                if stack2:
                    stack2.pop()
        if stack == stack2:
            return True
        return False