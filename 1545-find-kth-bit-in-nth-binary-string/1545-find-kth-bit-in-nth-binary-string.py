class Solution:
    def findKthBit(self, n: int, k: int) -> str:   
        def bit(n):
            if n == 1:
                return "0"
            prev = bit(n - 1)
            invert = ""
            for c in prev:
                if c == "0":
                    invert += "1"
                elif c == "1":
                    invert += "0"
            
            return prev + "1" + invert[::-1]
        
        S = bit(n)
        
        return S[k - 1]
            
            
            
            