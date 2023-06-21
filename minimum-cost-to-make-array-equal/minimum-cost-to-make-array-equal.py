class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs=sorted(list(zip(nums,cost)))
        cost_mid=sum(cost)/2
        cost_tmp=0
        for n,c in pairs:
            cost_tmp+=c
            if cost_tmp>=cost_mid:
                f=n
                break

        min_total_cost=0
        for n,c in pairs:
            min_total_cost+=abs(n-f)*c

        return min_total_cost                  