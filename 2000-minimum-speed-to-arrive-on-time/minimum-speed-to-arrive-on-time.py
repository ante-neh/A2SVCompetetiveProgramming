class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) >= hour + 1:
            return -1

        def isEnough(mid):
            time = 0
            for d in dist[:-1]:
                time += ceil(d / mid) 

            time += dist[-1] / mid
            return time <= hour

        left, right = 0, 10 ** 7

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid

            else:
                left = mid


        return left + 1