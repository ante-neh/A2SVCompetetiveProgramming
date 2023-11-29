class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def isEnough(mid):
            count = 0
            for t in time:
                count += mid // t

            return count >= totalTrips

        left, right = 0, 10 ** 20 + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid
            else:
                left = mid


        return left + 1