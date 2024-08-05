class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        cnt = {}
        for s in arr:
            if s in cnt:
                cnt[s] += 1
            else:
                cnt[s] = 1
                
        distincts = [s for s in arr if cnt[s] == 1]
        
        if k <= len(distincts):
            return distincts[k-1]
        else:
            return ""