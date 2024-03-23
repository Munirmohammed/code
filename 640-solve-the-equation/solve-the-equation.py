class Solution:
    def solveEquation(self, equation: str) -> str:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Parse the left side of the equation
        left_coefficient, left_constant = self.parse_side(left)
        
        # Parse the right side of the equation
        right_coefficient, right_constant = self.parse_side(right)
        
        # Calculate the final coefficients and constants
        coefficient = left_coefficient - right_coefficient
        constant = right_constant - left_constant
        
        # If coefficient is zero and constant is zero, infinite solutions
        if coefficient == 0 and constant == 0:
            return "Infinite solutions"
        # If coefficient is zero and constant is not zero, no solution
        elif coefficient == 0:
            return "No solution"
        # Otherwise, calculate the value of x
        else:
            return "x=" + str(constant // coefficient)
    
    def parse_side(self, side: str) -> Tuple[int, int]:
        coefficient = 0
        constant = 0
        sign = 1
        num = ""
        for char in side:
            if char.isdigit():
                num += char
            elif char == 'x':
                if num:
                    coefficient += int(num) * sign
                else:
                    coefficient += sign
                num = ""
            elif char in ('+', '-'):
                if num:
                    constant += int(num) * sign
                num = ""
                sign = 1 if char == '+' else -1
        if num:
            constant += int(num) * sign
        return coefficient, constant
