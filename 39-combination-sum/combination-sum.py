class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinationSums = []

        def dfs(cur, index, total):
            if total == target:
                combinationSums.append(cur[:])
                return 

            if total > target or index >= len(candidates):
                return 

            cur.append(candidates[index])
            dfs(cur, index, total + candidates[index])
            cur.pop()
            dfs(cur, index + 1, total)

        dfs([], 0, 0)

        return combinationSums
            