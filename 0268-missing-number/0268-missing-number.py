class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        isPresent = [True for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            isPresent[nums[i]] = False
            
        for i in range(len(isPresent)):
            if isPresent[i] == True:
                return i
            
        