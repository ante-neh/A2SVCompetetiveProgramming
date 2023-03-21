class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def helper(num1, num2, count):
            if num1 == 0 or num2 == 0:
                return count
            
            if num1 >= num2:
                return helper(num1 - num2, num2, count + 1)
            
            return helper(num1, num2 - num1, count + 1)
        
        return helper(num1, num2, 0)