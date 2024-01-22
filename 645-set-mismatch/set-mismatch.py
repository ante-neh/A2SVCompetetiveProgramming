class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0

        while i < len(nums):
            j = nums[i] - 1
            if j != i and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return [nums[i], i + 1]

                