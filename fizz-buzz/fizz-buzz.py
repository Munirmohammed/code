class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1,n+1):
            if i % 5 != 0 and i % 3 != 0:
                arr.append(str(i))
                
            elif i % 5 == 0 and i % 3 != 0:
                arr.append("Buzz")
                
            elif i % 3 == 0 and i % 5 != 0:
                arr.append("Fizz")
                
            if i % 5 == 0 and i % 3 == 0:
                arr.append("FizzBuzz")
            
        return arr
