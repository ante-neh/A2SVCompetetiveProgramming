class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            elif nums[mid] > nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid

                else:
                    left = mid

            elif nums[mid] < nums[left]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid
                
                else:
                    right = mid

            else:
                left += 1

        return nums[left] == target or( nums[left + 1] == target if left + 1 < len(nums) else False)