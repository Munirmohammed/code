class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Find the total number of elements in the array
        n = len(arr)
        
        # Count the occurrences of each element using Counter
        from collections import Counter
        count = Counter(arr)
        
        # Create a list of elements that appear more than 25% of the time
        frequent_elems = [key for key, value in count.items() if value > n//4]
        
        # Return the only element (there can be only one, given the input) from the list
        return frequent_elems[0] if frequent_elems else None