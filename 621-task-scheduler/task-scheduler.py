class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Task Frequencies
        task_counts = Counter(tasks)
        maxHeap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # Pair of (-cnt, idleTime)

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
