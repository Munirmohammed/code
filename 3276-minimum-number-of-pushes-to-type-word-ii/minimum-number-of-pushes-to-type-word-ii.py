class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        freq.sort(reverse=True)
        sz = next((i for i, x in enumerate(freq) if x == 0), 26)
        total_pushes = 0
        for i in range(sz):
            total_pushes += freq[i] * (i // 8 + 1)
        
        return total_pushes
        