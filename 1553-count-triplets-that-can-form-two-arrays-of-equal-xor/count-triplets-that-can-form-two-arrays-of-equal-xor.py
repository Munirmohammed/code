from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0] * (len(arr) + 1)  
        
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i] 
        
        count = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                xor_ij = prefix_xor[j + 1] ^ prefix_xor[i]
                
                if xor_ij == 0:
                    count += j - i  
                
        return count
