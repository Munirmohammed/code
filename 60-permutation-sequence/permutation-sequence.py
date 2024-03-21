class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            result = 1
            while n > 0:
                result *= n
                n -= 1
            return result
        
        nums = list(range(1, n+1))
        k -= 1
        result = []
        for i in range(n, 0, -1):
            nums.sort()
            index = k // factorial(i-1)
            result.append(str(nums[index]))
            nums.remove(nums[index])
            k %= factorial(i-1)
        return ''.join(result)