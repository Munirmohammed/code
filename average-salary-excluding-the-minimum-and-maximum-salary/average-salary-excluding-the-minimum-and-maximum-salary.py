class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        n = len(salary) - 2
        for i in range(1,len(salary)-1):
            sum = sum + salary[i]
        return sum / n