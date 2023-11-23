class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if mid * mid > num:
                right = mid

            else:
                left = mid

        
        return True if left * left == num else False 