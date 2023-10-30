class Solution:
    def countVowelPermutation(self, n: int) -> int:
        prevA, prevE, prevI, prevO, prevU = 1, 1, 1, 1, 1
        mod = 10**9 + 7 

        for length in range(2, n + 1):
            nextA = (prevE + prevU + prevI) % mod  
            nextE = (prevA + prevI) % mod  
            nextI = (prevE + prevO) % mod  
            nextO = prevI  
            nextU = (prevO + prevI) % mod  

            prevA, prevE, prevI, prevO, prevU = nextA, nextE, nextI, nextO, nextU

        return (prevA + prevE + prevI + prevO + prevU) % mod