class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        rem_days = n%7
        sum_ = 0
        i = 28
        for x in range(weeks):
            sum_ += i
            i += 7
        sum_ += (rem_days/2)*(2*(weeks+1)+(rem_days-1))

        return int(sum_)