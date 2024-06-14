class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Edge case: if k is 0, we need at least two 0s in the array
        if k == 0:
            return 0 in nums and nums.count(0) > 1

        # Initialize a dictionary to store the remainders and their indices
        remainder_to_index = {0: -1}  # The sum up to index -1 is considered to be 0

        # Initialize the running sum
        running_sum = 0

        for i, num in enumerate(nums):
            # Update the running sum
            running_sum += num

            # If k is not 0, we need to find the remainder of the running sum modulo k
            if k != 0:
                running_sum %= k

            # If the running sum has been seen before, we have found a subarray that sums to a multiple of k
            if running_sum in remainder_to_index:
                if i - remainder_to_index[running_sum] >= 2:  # The subarray size must be at least 2
                    return True
            else:
                # If the running sum has not been seen before, add it to the dictionary
                remainder_to_index[running_sum] = i

        # If we have gone through the entire array without finding a subarray that sums to a multiple of k, return False
        return False