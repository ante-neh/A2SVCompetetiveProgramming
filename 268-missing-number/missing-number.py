class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalXor = len(nums)

        for i in range(len(nums)):
            totalXor ^=( i ^ nums[i] )

        return totalXor