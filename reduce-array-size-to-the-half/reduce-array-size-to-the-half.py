class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x = Counter(arr)
        n = len(arr) // 2
        count = 0
        size = 0

        for key, value in x.most_common():
            print(value)
            count += value
            size += 1
            if count >= n:
                break

        return size
