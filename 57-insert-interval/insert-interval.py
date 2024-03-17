class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        result = []
        
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result