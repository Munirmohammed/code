class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        s = set()
        for val in dic.values():
            if val in s:
                return False
            s.add(val)
        return True
        