class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp =[[0]*len(nums) for _ in range(len(nums))]
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)): 
                if i == j:
                    dp[i][j] = nums[i]
                elif i+1 == j:
                    dp[i][j] = max(nums[i],nums[j])
                else:
                    dp[i][j] = max(nums[i] + min(dp[i+2][j],dp[i+1][j-1]), nums[j] + min(dp[i+1][j-1],dp[i][j-2]))
             
        return dp[0][-1] >= sum(nums) - dp[0][-1]