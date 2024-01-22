class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
        actual_sum = sum(nums)
        actual_sum_of_squares = sum(x ** 2 for x in nums)
        delta_sum = expected_sum - actual_sum
        delta_sum_of_squares = expected_sum_of_squares - actual_sum_of_squares
        duplicated_num = (delta_sum_of_squares - delta_sum ** 2) // (2 * delta_sum)
        missing_num = duplicated_num + delta_sum
        return [duplicated_num, missing_num]
