class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(mid):
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)

            return count >= k

        left, right = 0, (n * m) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if check(mid):
                right = mid

            else:
                left = mid 


        return left + 1