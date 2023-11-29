class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        count = 0
        arr = []
        
        for i in range(left, right+1):
            for j in str(i):
                if int(j) == 0 or i % int(j) != 0:
                    break
                count += 1
            
            if count == len(str(i)):
                arr.append(i)
            
            count = 0
        
        return arr

        