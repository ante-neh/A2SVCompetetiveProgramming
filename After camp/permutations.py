class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()

        def dfs(cur):
            if len(cur) == len(nums):
                result.append(cur[:])
                return

            for i in range(len(nums)):
                if not i in visited:
                    visited.add(i)
                    cur.append(nums[i])
                    dfs(cur)
                    visited.remove(i)
                    cur.pop()

        dfs([])

        return result