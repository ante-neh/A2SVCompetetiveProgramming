class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(m):
            day = 1
            total = 0

            for weight in weights:
                total += weight
                if total > m:
                    total = weight
                    day += 1

            return day <= days
            


        left, right = max(weights) - 1, sum(weights) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if isValid(mid):
                right = mid

            else:
                left = mid


        return left + 1