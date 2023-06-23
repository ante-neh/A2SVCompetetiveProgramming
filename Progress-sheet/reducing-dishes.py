class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        t = sum(satisfaction)
        n = len(satisfaction)
        dp = [0] * n
        
        dp[0] = sum([(i+1)*sat for i, sat in enumerate(satisfaction)])
        
        ans = max(dp[0], 0)
        
        for i in range(1, n):
            dp[i] = dp[i-1] - t
            t -= satisfaction[i-1]
            ans = max(ans, dp[i])
        
        return ans