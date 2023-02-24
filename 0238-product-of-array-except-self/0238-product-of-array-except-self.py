class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backPro = []
        product = 1
        forPro = 1
        res = []
        
        
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            backPro.append(product)
            
        backPro = backPro[::-1]
        
        for i in range(len(nums)-1):
            res.append(forPro * backPro[i + 1])
            forPro *= nums[i]
            
        res.append(forPro)
    
        return res
            