class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validIpAddresses = []
        part = []
        
        def backtrack(i):
            if i >= len(s):
                if len(part) == 4:
                    validIpAddresses.append(".".join(part[:]))
                return 
            
            for j in range(i, len(s)):
                val = int(s[i:j + 1])
                if 0 <= val and val <= 255 and self.isValid(s[i:j+1]):
                    part.append(str(val))
                    backtrack(j + 1)
                    part.pop()
                    
        backtrack(0)
                    
        return validIpAddresses
    
    def isValid(self, s):
        if len(s) > 1 and s.startswith("0"):
            return False
        return True