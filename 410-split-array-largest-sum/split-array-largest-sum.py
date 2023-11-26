class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(threshold):
            total = 0
            count = 1

            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1

            return count <= k


        left, right = max(nums) - 1, sum(nums) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid

        return left + 1