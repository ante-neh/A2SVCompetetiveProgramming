# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if not isBadVersion(mid):
                left = mid
                
            else:
                right = mid
                
        return right