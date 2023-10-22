class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            h_left, h_right = height[left], height[right]
            width = right - left
            min_height = min(h_left, h_right)
            max_area = max(max_area, width * min_height)
            
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return max_area
