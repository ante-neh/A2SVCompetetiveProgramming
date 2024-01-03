class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            correctPos = nums[i] - 1
            if correctPos != i and nums[i] != nums[correctPos]:
                nums[correctPos], nums[i] = nums[i], nums[correctPos]

            else:
                i += 1


        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return [nums[i] , i + 1]
        
