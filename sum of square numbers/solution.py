class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        
        while l < r:
            if l ** 2 + r ** 2 == c:
                return True
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                r -= 1
                
        return False