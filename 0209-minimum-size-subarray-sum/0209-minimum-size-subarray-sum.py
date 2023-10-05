class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = 0
        curSum = 0

        for right in range(len(nums)):
            curSum += nums[right]

            while curSum >= target:
                minLength = min(minLength, right - left + 1)
                curSum -= nums[left]
                left += 1

        return 0 if minLength == float('inf') else minLength