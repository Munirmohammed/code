class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        rolls_sum = sum(rolls)
        missing_sum = total_sum - rolls_sum  
        if missing_sum < n or missing_sum > 6 * n:
            return []
        missing = [1] * n
        remaining_sum = missing_sum - n  
        
        for i in range(n):
            add = min(remaining_sum, 5)
            missing[i] += add
            remaining_sum -= add
            if remaining_sum == 0:
                break
        
        return missing