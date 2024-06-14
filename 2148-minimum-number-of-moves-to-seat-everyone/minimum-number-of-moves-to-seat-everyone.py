class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        total_moves = 0
        for s, p in zip(students, seats):
            total_moves += abs(s - p)
        return total_moves