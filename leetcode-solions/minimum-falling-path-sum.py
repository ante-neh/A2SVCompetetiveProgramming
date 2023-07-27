class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        minFallingPathSum = float('inf')


        def dp(r, c):
            if c < 0 or c == len(matrix):
                return float('inf')
            
            if r == len(matrix) - 1:
                return matrix[r][c]

            if (r, c) not in memo:
                memo[(r, c)] = matrix[r][c] + min(dp(r + 1, c), dp(r + 1, c + 1), dp(r + 1, c - 1))

            return memo[(r, c)]

        for i in range(len(matrix)):
            minFallingPathSum = min(minFallingPathSum, dp(0, i))

        return minFallingPathSum
         

