class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        currentSum = sum(nums[:k])
        maxSum = currentSum

        for right in range(k,len(nums)):
            maxSum = max(maxSum, currentSum)
            currentSum += nums[right]
            currentSum -= nums[left]
            left += 1
            
        return maxSum / k