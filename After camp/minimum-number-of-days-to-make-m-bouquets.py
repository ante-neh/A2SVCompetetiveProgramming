class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        def isValid(mid):
            bouquet, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > mid:
                    flowers = 0

                else:
                    bouquet += (flowers + 1) // k
                    flowers = (flowers + 1) % k

            return bouquet >= m

        left, right = 0, max(bloomDay) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if isValid(mid):
                right = mid

            else:
                left = mid


        return left + 1