class Solution:
    def trap(self, height: List[int]) -> int:

        def trap_with_range(start, end, dir, wall_condition):
            volume = 0       
            temp_volume = 0  
            wall = start     
            for i in range(start, end + dir, dir):
                if wall_condition(height[i], height[wall]):
                    wall = i
                    volume += temp_volume
                    temp_volume = 0
                else:
                    temp_volume += height[wall] - height[i]
            return volume
        left_trap = trap_with_range(0, len(height) - 1, 1, lambda a, b: a >= b)
        right_trap = trap_with_range(len(height) - 1, 0, -1, lambda a, b: a > b)

        return  left_trap + right_trap