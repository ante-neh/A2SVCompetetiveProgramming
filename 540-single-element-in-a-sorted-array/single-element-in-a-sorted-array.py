class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 == len(nums) or nums[mid] != nums[mid + 1]):
                return nums[mid]

            if nums[mid] == nums[mid - 1] and (mid - 1) % 2:
                right = mid

            elif nums[mid] != nums[mid - 1] and (mid) % 2:
                right = mid

            else:
                left = mid


                
            

            

            