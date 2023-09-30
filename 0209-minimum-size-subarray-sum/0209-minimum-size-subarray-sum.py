class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        left = 0
        curSum = 0

        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:
                curSum -= nums[left]
                minLen = min(minLen, right - left + 1)
                left += 1
                
        return 0 if minLen == float('inf') else minLen