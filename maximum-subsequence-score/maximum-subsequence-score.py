class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == len(nums1):
            return (sum(nums1) * min(nums2))
        k_sum = 0   
        ans = 0
        heap: List[Tuple[int, int]] = []
        for num1, num2 in sorted(zip(nums1, nums2), reverse = True):
            k_sum += num1
            heapq.heappush(heap, (num2, num1))
            if len(heap) == k:
                num2, num1 = heapq.heappop(heap)
                ans = max(ans, k_sum * num2)
                k_sum -= num1
        return ans
        