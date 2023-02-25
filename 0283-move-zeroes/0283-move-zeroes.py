class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        write, read = 0, 0
        
        while write < len(nums):
            if nums[write] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                read += 1
                
            write += 1