class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1,n + 1))
        
        preSum = nums[0]
        totalSum = sum(nums)
        if preSum == totalSum:
            return nums[0]
        
        for i in range(1,len(nums)):
            preSum += nums[i]
            totalSum -= nums[i - 1]
            
            if preSum == totalSum:
                return nums[i]
            
        return -1