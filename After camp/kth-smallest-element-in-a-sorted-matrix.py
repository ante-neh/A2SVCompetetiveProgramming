class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mid):
            count = 0

            for row in matrix:
                count += bisect.bisect_right(row, mid)

            return count >= k

        left, right = matrix[0][0] - 1, matrix[-1][-1] + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid


        return left + 1