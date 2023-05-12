class Solution:
    def lengthLongestPath(self, s: str) -> int:
        paths = s.split('\n')
        stack, ans = [0], 0 
        for path in paths:
            p = path.split('\t')
            depth, name = len(p) - 1, p[-1]
            while len(stack) > depth + 1:
                stack.pop()
            if '.' in name: 
                ans = max(ans, stack[-1] + len(name))
            else: 
                stack.append(stack[-1] + len(name) + 1)
        return ans