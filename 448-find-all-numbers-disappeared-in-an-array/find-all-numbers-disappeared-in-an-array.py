class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums):
            correctPos = nums[i] - 1
            if correctPos != i and nums[i] != nums[correctPos]:
                nums[correctPos], nums[i] = nums[i], nums[correctPos]
            else:
                i += 1
        
        result = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result
            