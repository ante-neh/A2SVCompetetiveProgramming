class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1

        def isValid(mid):
            bouquet, count = 0, 0
            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1
                else:
                    bouquet += count // k
                    count = 0

            bouquet += count // k
            
            return bouquet >= m

        left, right = 0, max(bloomDay) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if isValid(mid):
                right = mid

            else:
                left = mid


        return left + 1