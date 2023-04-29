class Solution:
    def maxProfit(self, prices: list[int]) -> int: 
        nostock, stock, cool = 0,-prices[0],0  
        for p in prices[1:]: 
            nostock, stock, cool = (max(nostock,cool),max(stock,nostock-p),stock+p)
        return max(nostock, stock,cool)                                             