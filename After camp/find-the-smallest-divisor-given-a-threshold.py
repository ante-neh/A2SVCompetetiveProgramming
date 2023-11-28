class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(mid):
            sum = 0
            for num in nums:
                sum += ceil(num / mid)

            return sum <= threshold


        left, right = 0, max(nums) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if isValid(mid):
                right = mid
            else:
                left = mid

        return left + 1