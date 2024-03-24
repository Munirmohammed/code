class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
    
        # Create a hash table to store the counts of elements
        count_table = {}
        
        for element in arr:
            if element in count_table:
                count_table[element] += 1
            else:
                count_table[element] = 1
        
        # Iterate through the hash table and find the element that appears more than 25% of the time
        for key, value in count_table.items():
            if value > n//4:
                return key
        
        return -1  # return -1 if no element is found

                  
                  
