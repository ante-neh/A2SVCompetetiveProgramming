class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, minLen = 0, float('inf')
        sum = 0
        
        for r in range(len(nums)):
            sum += nums[r]
            
            while sum >= target:
                minLen = min(minLen, r - l + 1)
                sum -= nums[l]
                l += 1
                
        return minLen if minLen != float("inf") else 0