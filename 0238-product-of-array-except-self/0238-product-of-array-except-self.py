class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backPro = []
        backProduct = 1
        forPro = 1
        
        for i in range(len(nums) - 1, -1, -1):
            backProduct *= nums[i]
            backPro.append(backProduct)
            
        for i in range(len(nums)):
            forPro *= nums[i]
            nums[i] = forPro
        
        backPro = backPro[::-1]
        forPro = 1
        for i in range(len(nums) - 1):
            backPro[i] = forPro * backPro[i + 1]
            forPro = nums[i]
            
        backPro[-1] = forPro
        
        return backPro
        
            