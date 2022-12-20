class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        
        for c , v in t.items():
            if s[c] != v:
                return c
            
        
        