class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = n & 1
        n >>= 1
        while n > 0:
            cur = n & 1
            if cur == res:
                return False
            
            res = cur
            n >>= 1
            
        return True