class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(m):
            time = 0

            for pile in piles:
                time += ceil(pile / m)

            return time <= h

        left, right = 0, sum(piles) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid

            else:
                left = mid

        return left + 1