class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        time = [0] * 1001

        for trip in trips:
            num, start, end = trip
            for i in range(start, end):
                time[i] += num
                if time[i] > capacity:
                    return False
        return True