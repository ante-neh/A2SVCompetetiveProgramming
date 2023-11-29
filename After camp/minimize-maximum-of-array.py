class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefixSum = 0
        minNum = 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            minNum = max(minNum, ceil(prefixSum / (i + 1)))

        return minNum