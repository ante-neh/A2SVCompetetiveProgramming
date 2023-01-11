class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        
        l, r = 0, 1
        
        while l < len(nums) and r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                
            if nums[l] != 0:
                l += 1
                
            if nums[r] == 0 or r <= l:
                r += 1
                
        return nums