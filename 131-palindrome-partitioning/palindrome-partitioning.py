class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def helper(s, current):
            if not s:
                result.append(current)
                return
            for i in range(1, len(s)+1):
                if self.is_palindrome(s[:i]):
                    helper(s[i:], current + [s[:i]])
        helper(s, [])
        return result