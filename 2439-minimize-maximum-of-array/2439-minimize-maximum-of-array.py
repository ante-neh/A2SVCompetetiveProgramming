class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)
        optimal = ceil(totalSum / n)
        i = n - 1
        
        while i - 1 > -1:
            if nums[i] > optimal:
                diff = nums[i] - optimal
                nums[i] -= diff
                nums[i - 1] += diff
                
            totalSum -= nums[i]
            optimal = ceil((totalSum) / (n - 1))
            n -= 1
            i -= 1
            
        return max(nums)
            
            
            
            
            
            