class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(capital))]
        projects.sort()
        pq = []
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(pq, -projects[i][1])
                i += 1
            if not pq:
                break
            w -= heapq.heappop(pq)
            k -= 1
        return w