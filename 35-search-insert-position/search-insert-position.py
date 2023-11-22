class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid
            
            else:
                left = mid

        return left if nums[left] == target else left + 1

            