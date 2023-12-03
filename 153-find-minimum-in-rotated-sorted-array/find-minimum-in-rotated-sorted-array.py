class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right] and nums[left] > nums[right]:
                left = mid

            elif nums[mid] > nums[left] and nums[right] > nums[left]:
                right = mid 

            elif nums[mid] < nums[left] and nums[mid] < nums[right] and nums[left] > nums[right]:
                right = mid 

            else:
                right = mid

        return min(nums[left], nums[left + 1]) if left + 1 < len(nums) else nums[left]

