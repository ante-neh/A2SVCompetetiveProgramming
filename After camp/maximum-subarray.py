class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float("-inf")

        for num in nums:
            curSum = max(curSum + num, num)
            maxSum = max(maxSum, curSum)

        return maxSum