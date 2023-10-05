class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        numberOfZeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfZeros += 1

            while numberOfZeros > 1:
                if nums[left] == 0:
                    numberOfZeros -= 1

                left += 1

            maxLength = max(maxLength, right - left  + 1)

        return maxLength - 1 if maxLength > 0 else 0