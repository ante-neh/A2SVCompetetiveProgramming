class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]