class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = 0
        actual_sum_of_squares = 0
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = sum(num * num for num in range(1, n + 1))
        
        for num in nums:
            actual_sum += num
            actual_sum_of_squares += num * num
        
        sum_diff = actual_sum - expected_sum
        sum_of_squares_diff = actual_sum_of_squares - expected_sum_of_squares
        
        duplicate = (sum_of_squares_diff // sum_diff + sum_diff) // 2
        
        missing = duplicate - sum_diff
        
        return [duplicate, missing]
