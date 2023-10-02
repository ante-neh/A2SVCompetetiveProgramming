class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longestNiceSubarray = 1
        left = 0
        currentGroup = 0

        for right in range(len(nums)):
            if currentGroup & nums[right] == 0:
                currentGroup |= nums[right]
                longestNiceSubarray = max(longestNiceSubarray, right - left + 1)
                continue

            while left < right and currentGroup & nums[right] != 0:
                currentGroup &= ~nums[left]
                left += 1

            currentGroup |= nums[right]

        return longestNiceSubarray
