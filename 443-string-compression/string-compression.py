class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        n = len(chars)
        i = 0  
        count = 1  
        for j in range(1, n):
            if chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1
        chars[i] = chars[n - 1]
        i += 1
        if count > 1:
            for digit in str(count):
                chars[i] = digit
                i += 1

        return i
