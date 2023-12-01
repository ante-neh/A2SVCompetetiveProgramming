class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isEnough(mid):
            count = 0
            for num in nums:
                count += ceil((num / mid)) - 1

            return count <= maxOperations


        left, right = 0, max(nums) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isEnough(mid):
                right = mid

            else:
                left = mid


        return left + 1