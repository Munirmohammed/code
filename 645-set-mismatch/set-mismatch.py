class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Calculate the sum of all numbers and the sum of squares
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum_of_squares = sum(num * num for num in nums)
        expected_sum_of_squares = sum(num * num for num in range(1, n + 1))
        
        # Calculate the difference between actual and expected sums
        sum_diff = actual_sum - expected_sum
        sum_of_squares_diff = actual_sum_of_squares - expected_sum_of_squares
        
        # Calculate the duplicate number
        duplicate = (sum_of_squares_diff // sum_diff + sum_diff) // 2
        
        # Calculate the missing number
        missing = duplicate - sum_diff
        
        return [duplicate, missing]
