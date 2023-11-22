class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)
        result = [-1, -1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid

            else:
                left = mid

        
        if left != -1 and nums[left] == target:
            result[1] = left

        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target <= nums[mid]:
                right = mid

            else:
                left = mid

        if result[1] != -1:
            result[0] = left + 1

        return result