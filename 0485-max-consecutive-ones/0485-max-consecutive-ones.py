class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        left = 0
        count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1

            while count > 0:
                if nums[left] == 0:
                    count -= 1
                
                left += 1

            maxLength = max(maxLength ,right - left + 1)

        return maxLength