class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_len = 0
        table = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            if count in table:
                max_len = max(max_len, i - table[count])
            else:
                table[count] = i
        return max_len
        