class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        count = 0
        j = 0
        for i in range(1, len(digits)+1):
            
            j = j*10
            if j ==0:
                j = 1
            count = count + digits[len(digits)-i]*j
            print(count)
        
        count = count + 1 

        # print(count)
        digits = [int(i) for i in str(count)]

        return digits
            
