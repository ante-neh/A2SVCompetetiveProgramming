class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        left = 0
        result = []

        for right in range(len(nums)):
            if right - left + 1 == 3:
                if nums[right] - nums[left] <= k:
                    result.append(nums[left:right + 1])
                    left = right + 1

                else:
                    left += 1

        return result if len(result) == len(nums) // 3 else []