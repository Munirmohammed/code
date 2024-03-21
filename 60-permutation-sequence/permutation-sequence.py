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
        while n > 0:
            factorial_n_minus_1 = factorial(n-1)
            index, k = divmod(k, factorial_n_minus_1)
            result.append(str(nums[index]))
            nums.pop(index)
            n -= 1
        return ''.join(result)