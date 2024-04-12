class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = height[0]
        r_max = height[-1] 
        n = len(height)
        left = 1
        right = n-2

        if n <= 2:
            return 0

        water = 0
        while left <= right:
            if l_max <= r_max:
                water += max(0, min(l_max, r_max) - height[left])
                l_max = max(l_max, height[left])
                left += 1
            else:
                water += max(0, min(l_max, r_max) - height[right])
                r_max = max(r_max, height[right])
                right -= 1
                
        return water
        