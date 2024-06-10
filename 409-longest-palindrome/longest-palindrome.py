class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        
        # Count the frequency of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Calculate the length of the longest palindrome
        length = 0
        odd_count = 0
        for count in char_count.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_count += 1
        
        # If there's at least one character with an odd count, we can add 1 to the length
        if odd_count > 0:
            length += 1
        
        return length