class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            stones = sorted(stones,reverse = True)
            if len(stones) == 1:
                return stones[0]
            elif len(stones) == 0:
                return 0
            first = stones.pop(0)
            sec = stones.pop(0)
            if first == sec:
                continue
            else:
                stones.append(first-sec)
                print(stones)