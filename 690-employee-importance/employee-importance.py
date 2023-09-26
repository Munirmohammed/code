from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = emp
            
        q = deque([emp_map[id]])
        imp = 0
        while len(q)!=0:
            e = q.popleft()
            imp += e.importance
            for subordinate in e.subordinates:
                q.append(emp_map[subordinate])
        return imp