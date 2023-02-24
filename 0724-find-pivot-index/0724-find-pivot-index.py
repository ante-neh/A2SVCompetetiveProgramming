class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            if preSum == total - nums[i]:
                return i
            
            preSum += nums[i]
            total -= nums[i]
            
        return -1