class Solution:
    @staticmethod
    def minFlips(a: int, b: int, c: int) -> int:
        flips = 0

        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    flips += 1
                else:
                    if bit_a == 1:
                        flips += 1
                    if bit_b == 1:
                        flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips