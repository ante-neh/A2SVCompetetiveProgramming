class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        minDifference = float("inf")

        for right in range(len(nums)):
            if right - left + 1 == k:
                minDifference = min(minDifference, max(nums[left:right + 1]) - min(nums[left:right + 1]))
                left += 1

        return minDifference