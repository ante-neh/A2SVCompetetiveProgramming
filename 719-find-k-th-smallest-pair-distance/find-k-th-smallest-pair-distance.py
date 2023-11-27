class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def isValid(mid):
            count = 0
            j, i = 0, 0
            while i < len(nums) or j < len(nums):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1

                count += j - i - 1
                i += 1

            return count >= k 

        left, right = -1, max(nums) - min(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid

            else:
                left = mid


        return left + 1