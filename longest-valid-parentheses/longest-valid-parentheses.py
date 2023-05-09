class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        maxlength = 0
        for i in range(len(s)):
            t = st[-1]
            if t != -1 and s[i] == ')' and s[t] == '(':
                st.pop()
                maxlength = max(maxlength, i - st[-1])
            else:
                st.append(i)
        return maxlength