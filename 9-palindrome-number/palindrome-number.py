class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reversed_x = 0
        original_x = x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        return original_x == reversed_x