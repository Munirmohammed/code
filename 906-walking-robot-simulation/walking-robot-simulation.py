class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        xcor = 0
        ycor = 0
        moveX = 0
        moveY = 1
        obstacle_set = set(map(tuple, obstacles))
        max_distance_squared = 0
        
        for k in commands:
            if k > 0:
                for _ in range(k):
                    if (xcor + moveX, ycor + moveY) not in obstacle_set:
                        xcor += moveX
                        ycor += moveY
                        max_distance_squared = max(max_distance_squared, xcor * xcor + ycor * ycor)
            elif k == -1:
                moveX, moveY = moveY, -moveX
            elif k == -2:
                moveX, moveY = -moveY, moveX
        
        return max_distance_squared