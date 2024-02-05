class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        t = 0
        for i in s:
            if c[i] == 1:
                return t
            t += 1
        return -1

        