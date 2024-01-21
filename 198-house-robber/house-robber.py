class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i > len(nums) - 1:
                return 0

            if i == len(nums) - 1:
                return nums[-1]

            if not i in memo:
                memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))

            return memo[i]

        return dp(0)