class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numberOfZeros = 0
        left = 0
        maxLength = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfZeros += 1

            while numberOfZeros > k:
                if nums[left] == 0:
                    numberOfZeros -= 1
                
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
                