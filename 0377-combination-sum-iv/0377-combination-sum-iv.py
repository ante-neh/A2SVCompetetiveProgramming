class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for t in range(min(nums), target + 1):
            for n in nums:
                if n <= t:
                    dp[t] += dp[t-n]
            
        return dp[-1]