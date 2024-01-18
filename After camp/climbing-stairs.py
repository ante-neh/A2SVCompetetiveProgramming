class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            nonlocal memo
            if n <= 2:
                return n

            if not n in  memo:
                memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        return dfs(n)

        