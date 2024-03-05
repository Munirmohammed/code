class Solution(object):
    def minimumLength(self, s):
        left = 0
        right = len(s) - 1
        
        while left < right and s[left] == s[right]:
            current = s[left]
            while left <= right and s[left] == current:
                left += 1
            while right >= left and s[right] == current:
                right -= 1
        
        return max(0, right - left + 1)