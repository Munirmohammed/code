class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        if x == y: return True
        return False