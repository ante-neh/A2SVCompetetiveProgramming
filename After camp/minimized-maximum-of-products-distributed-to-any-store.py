class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def isValid(mid):
            sum = 0
            for quantity in quantities:
                sum += ceil(quantity / mid)

            return sum <= n

        left, right = 0, sum(quantities) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid

            else:
                left = mid

        return left + 1