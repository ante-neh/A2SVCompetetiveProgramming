class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dp(row, col):
            if row < 0 or col < 0 or col >= len(matrix[0]) or row >= (len(matrix)):
                return float("inf")

            if row == len(matrix) - 1:
                return matrix[-1][col]
            if not (row, col ) in memo:
                memo[(row, col)] = matrix[row][col] + min(dp(row + 1, col - 1), dp(row + 1, col), dp(row + 1, col + 1))

            return memo[(row, col)]

        minFallingPathSum = float("inf")

        for i in range(len(matrix[0])):
            minFallingPathSum = min(minFallingPathSum, dp(0, i))

        return minFallingPathSum