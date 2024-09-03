class Solution(object): 
    def getValue(self, s):
        total = sum(int(ch) for ch in s)
        return str(total)

    def getLucky(self, s, k):
        converted = ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        for _ in range(k):
            converted = self.getValue(converted)
        return int(converted)