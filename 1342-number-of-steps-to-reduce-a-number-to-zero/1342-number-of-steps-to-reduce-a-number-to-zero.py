class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        def helper(num, c):
            if num == 0:
                return c
            
            if num % 2 == 0:
                return helper(num // 2, c + 1)
            
            return helper(num - 1, c + 1)
        
        
        
        return helper(num, 0)
            