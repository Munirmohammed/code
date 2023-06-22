class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        x0 = 0
        x1 = float('-inf')

        for i in range(N):
            x0 = max(x0, x1 + prices[i])
            x1 = max(x1, x0 - prices[i] - fee)
        return max(x0, x1)
