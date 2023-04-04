class Solution:
    def countArrangement(self, n: int) -> int:
        
        res = 0
        
        def backtrack(used, idx):
            nonlocal res
            if idx == n + 1:
                res += 1
                return 
            
            for i in range(n):
                if used[i+1] or ((idx % (i + 1)) != 0 and ((i + 1) % idx) != 0) :
                    continue
                    
                used[i+1] = True
                backtrack(used, idx + 1)
                used[i+1] = False
                
        backtrack([False] * (n + 1), 1)
        
        return res