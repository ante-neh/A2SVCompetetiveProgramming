class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = [0]

        for num in nums:
            prefixSum.append(num + prefixSum[-1])

        minValue = float("inf")
        maxSubArray = float("-inf")

        for i in range(1, len(nums) + 1):
            minValue = min(minValue, prefixSum[i - 1])
            maxSubArray = max(maxSubArray, prefixSum[i] - minValue)

        return maxSubArray