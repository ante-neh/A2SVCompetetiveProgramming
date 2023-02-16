class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sIndex = {}
        res = []
        
        for i in range(len(s)):
            sIndex[s[i]] = i
        
        index = l = r = 0
        
        while index < len(s):
            r = max(r, sIndex[s[index]])
            if r == index:
                res.append(r - l + 1)
                l = r+1
                r += 1
            index += 1
        return res