class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxErasureValue = 0
        curSum = 0
        left = 0
        numsCount = set()

        for right in range(len(nums)):
            curSum += nums[right]

            while nums[right] in numsCount:
                curSum -= nums[left]
                numsCount.remove(nums[left])
                left += 1
                
            numsCount.add(nums[right])
            maxErasureValue = max(maxErasureValue, curSum)

        return maxErasureValue