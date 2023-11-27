class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def isValid(mid):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left

            return count >= k

        left, right = -1, nums[-1] - nums[0]

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid


        return left + 1