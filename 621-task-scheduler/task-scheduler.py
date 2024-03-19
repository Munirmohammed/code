class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [-count for count in Counter(tasks).values()]
        heapq.heapify(task_counts)

        time = 0
        cooldown = deque()

        while task_counts or cooldown:
            time += 1

            if cooldown and cooldown[0][0] == time - n - 1:
                heapq.heappush(task_counts, cooldown.popleft()[1])

            if task_counts:
                remaining_count = heapq.heappop(task_counts) + 1
                if remaining_count < 0:
                    cooldown.append((time, remaining_count))

        return time
