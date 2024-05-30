class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)  #Convert binary string to integer
        steps = 0

        while num > 1:  #Loop until num equals 1
            if num % 2 == 0: 
                num //= 2 # If even, divide by 2
            else: 
                num += 1 # If odd, add 1
            steps += 1 # Increment steps count
        return steps