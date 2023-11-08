class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            
            max_freq = max(count.values())
            
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[s[left]] -= 1 
                left += 1
                
            longest = max(longest, right - left + 1)
            
        return longest