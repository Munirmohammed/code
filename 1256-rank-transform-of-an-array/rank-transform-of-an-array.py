class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))  # Sort and remove duplicates
        
        # Create a dictionary to store ranks
        rank_dict = {}
        rank = 1
        for val in arr_sorted:
            rank_dict[val] = rank
            rank += 1
        
        # Map ranks to original array
        return [rank_dict[val] for val in arr]
