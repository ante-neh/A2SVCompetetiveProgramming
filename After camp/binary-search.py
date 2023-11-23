class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        return left if nums[left] == target else -1