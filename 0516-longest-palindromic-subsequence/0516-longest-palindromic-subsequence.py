class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1

        for length in range(1, len(s)):
            i = 0
            while i + length < len(s):
                j = i + length
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

                i += 1

        return dp[0][-1]

        