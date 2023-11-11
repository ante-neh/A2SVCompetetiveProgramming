class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)
            total += num

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum 