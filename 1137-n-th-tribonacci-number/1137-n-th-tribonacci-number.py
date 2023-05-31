class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        
        dp = [0 for i in range(n + 1)]
        
        dp[0], dp[1], dp[2] = 0, 1, 1
        
        for num in range(3, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2] + dp[num - 3]
            
        return dp[-1]

        