class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_length = -1
        char_dict = {}
        for i, char in enumerate(s):
            if char in char_dict:
                max_length = max(max_length, i - char_dict[char] - 1)
            else:
                char_dict[char] = i
        return max_length