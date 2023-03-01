class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(strs):
            strs = list(strs)
            for i in range(len(strs)):
                if strs[i] == "0":
                    strs[i] = "1"
                else:
                    strs[i] = "0"
                    
            return "".join(strs)
        
        def reverse(strs):
            return strs[::-1]
        
        def helper(j, bits):
            if j == n:
                return bits
            else:
                bits.append(bits[j - 1] + "1" + reverse(invert(bits[j - 1])))
                return helper(j + 1, bits)
                
                
        bits = ["0"]
        result = helper(1, bits)
        return result[n - 1][k - 1]
        
            
            
            
            