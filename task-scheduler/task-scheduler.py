class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        values = list(Counter(tasks).values())
        max_val = max(values)
        ties = values.count(max_val)
        return max((max_val - 1) * (n + 1) + ties, len(tasks))