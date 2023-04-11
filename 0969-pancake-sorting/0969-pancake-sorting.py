class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def pancake(nums):
            if len(nums) > 0:
                maxVal = max(nums)
                index = nums.index(maxVal)
                res.append(index + 1)
                nums[:index + 1] = nums[:index + 1][::-1]
                res.append(maxVal)
                nums = nums[::-1]
                pancake(nums[:-1])
            
        pancake(arr)
        
        return res
            
        
            