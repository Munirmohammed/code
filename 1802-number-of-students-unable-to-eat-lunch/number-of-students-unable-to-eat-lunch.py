from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circular_students = deque()
        square_students = deque()
        
        for i, pref in enumerate(students):
            if pref == 0:
                circular_students.append(i)
            else:
                square_students.append(i)
        
        for sandwich in sandwiches:
            if sandwich == 0:
                if circular_students:
                    circular_students.popleft()
                else:
                    break
            else:
                if square_students:
                    square_students.popleft()
                else:
                    break
        return len(circular_students) + len(square_students)