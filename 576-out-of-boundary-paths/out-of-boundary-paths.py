class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        mod = 10 ** 9 + 7
        def dfs(r, c, moves):
            if r < 0 or r == m or c < 0 or c == n:
                return 1
            
            if moves == 0:
                return 0

            if (r, c , moves) in memo:
                return memo[(r, c, moves)]

            memo[(r, c, moves)] = ((dfs(r + 1, c , moves - 1) + dfs(r - 1, c, moves - 1)) % mod +
            (dfs(r, c + 1, moves - 1) + dfs(r, c - 1, moves - 1)) % mod) % mod

            return memo[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)

            