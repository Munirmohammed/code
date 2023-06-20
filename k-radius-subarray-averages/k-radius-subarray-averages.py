class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        avgs = [-1] * n
        window_size = 2 * k + 1

        if n < window_size:
            return avgs

        window = nums[k]
        for i in range(1, k + 1):
            window += nums[k + i] + nums[k - i]
        avgs[k] = window // window_size

        for i in range(k + 1, n - k):
            window += nums[i + k] - nums[i - k - 1]
            avgs[i] = window // window_size

        return avgs