class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        queue = deque([('0000', 0)])
        
        while queue:
            current, steps = queue.popleft()
            
            if current == target:
                return steps
            
            for i in range(4):
                for increment in (-1, 1):
                    next_state = current[:i] + str((int(current[i]) + increment) % 10) + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        return -1

        