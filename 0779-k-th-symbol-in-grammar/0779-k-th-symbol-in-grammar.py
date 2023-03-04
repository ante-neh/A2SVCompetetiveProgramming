class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #0
        #01
        #0110
        #01101001
        #0110100110010110
        #01101001100101101001011001101001
        
        
        def symbol(row, curr):
            if row == 1:
                return 0
            
            prev = symbol(row - 1, (curr // 2 + curr % 2))
            
            if prev == 1:
                if curr % 2 == 1:
                    return 1
                
                return 0
            
            else:
                if curr % 2 == 1:
                    return 0
                
                return 1
            
        return symbol(n, k)
