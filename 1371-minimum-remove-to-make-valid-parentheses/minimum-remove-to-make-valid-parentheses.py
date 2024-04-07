class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result, q = [], 0
        for c in s:
            if q or c != ')':
                q += (c == '(') - (c == ')')
                result.append(c)

        return ''.join(''.join(result).rsplit('(', q))