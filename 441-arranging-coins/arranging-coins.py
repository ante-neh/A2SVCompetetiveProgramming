class Solution:
    def arrangeCoins(self, n: int) -> int:
        def isEnough(mid):
            row = (mid / 2 ) * (mid + 1)
            return row <= n

        left, right = 1,  n 

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                left = mid

            else:
                right = mid 


        return left
