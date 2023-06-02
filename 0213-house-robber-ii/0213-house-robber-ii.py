class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        if len(nums) == 1:
            return nums[0]
        
        def dp(i, arr):
            if i == 0:
                return arr[i]
            
            if i == 1:
                return max(arr[1], arr[0])
            
            if i not in memo:
                memo[i] = max(dp(i - 1, arr), dp(i - 2, arr) + arr[i])
                
            return memo[i]
        
        arr = nums[1:]
        left = dp(len(arr) - 1, arr)

        arr = nums[:-1]
        memo = {}
        right = dp(len(arr) - 1, arr)
        
        return max(left, right)