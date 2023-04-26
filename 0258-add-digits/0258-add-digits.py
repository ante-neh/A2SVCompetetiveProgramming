class Solution:
    def addDigits(self, num: int) -> int:
        def add(n):
            sum = 0
            while n > 0:
                sum += n % 10
                n //= 10
                
            return sum
        
        def helper(num):
            if num < 10:
                return num
            
            return helper(add(num))
        
        return helper(num)
            