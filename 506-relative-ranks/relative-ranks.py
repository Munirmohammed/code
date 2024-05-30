import numpy as np

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        n = len(score)
        
        # Get the indices that would sort the array score
        sorted_indices = np.argsort(score)[::-1]
        
        answer = [None] * n
        for idx in range(n):
            rank = idx + 1
            if rank > 3:
                answer[sorted_indices[idx]] = str(rank)
            else:
                answer[sorted_indices[idx]] = ranks[rank-1]
                
        return answer