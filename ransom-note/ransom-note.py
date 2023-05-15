class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = Counter(magazine) 
        y = Counter(ransomNote)
        print(y & x)
        if y & x == y:
            return True
        return False
        
