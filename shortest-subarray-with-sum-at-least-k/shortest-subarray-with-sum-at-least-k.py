class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = 0
        queue = collections.deque([(-1,0)])
        res = n + 1
        for i in range(n):
            preSum += nums[i]
            if nums[i] > 0:
                while queue and preSum - queue[0][1] >= k:
                    res = min(res, i - queue.popleft()[0])
            else:
                while queue and preSum < queue[-1][1]:
                    queue.pop()
            queue.append((i, preSum))
        return res if res <= n else -1