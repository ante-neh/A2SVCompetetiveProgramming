class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s = list(s)
            for i in range(len(s)):
                if s[i] == "0":
                    s[i] = "1"
                else:
                    s[i] = "0"
                    
                return "".join(s)
            
        def bit(n):
            if n == 1:
                return "0"
            prev = bit(n - 1)
            
            return prev + "1" + invert(prev)
        
        S = bit(n)
        
        return S[k - 1]