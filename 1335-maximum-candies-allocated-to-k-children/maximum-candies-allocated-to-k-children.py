class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def isValid(mid):
            count = 0
            for pile in candies:
                count += pile // mid

            return count >= k


        left, right = 0, sum(candies) // k + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                left = mid

            else:
                right = mid

        return left 

            