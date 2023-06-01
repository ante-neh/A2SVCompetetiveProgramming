class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(curSum, i):
            if i >= len(nums):
                if curSum == target:
                    return 1
                
                return 0
            
            if (curSum, i) in memo:
                return memo[(curSum, i)]
            
            m = dp(curSum + nums[i], i + 1) 
            n = dp(curSum - nums[i], i + 1)
            
            memo[(curSum, i)] = n + m
            
            return n + m
            
        return dp(0, 0)