class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(cur, i):
            if i > len(nums):
                return

            if i <= len(nums):
                subsets.append(cur[:])

            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(cur, j + 1)
                cur.pop()

        dfs([], 0)

        return subsets