class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sCount, pCount = Counter(s[:len(p)]), Counter(p)
        result = []
        
        if sCount == pCount:
            result.append(0)
            
        l = 0
        
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
                
            if sCount == pCount:
                result.append(l)
                
        return result