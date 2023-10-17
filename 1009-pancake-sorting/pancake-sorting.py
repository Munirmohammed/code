class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def flip(k):
            result.append(k)
            l, r = 0, k-1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1

        for i in range(len(arr)):
            maxx, k = -math.inf, -1
            for j in range(len(arr)-i):
                if arr[j] > maxx:
                    maxx = arr[j]
                    k = j + 1
            
            flip(k)
            flip(len(arr)-i)
        
        return result