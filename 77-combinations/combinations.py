class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(cur, index):
            if len(cur) == k:
                combinations.append(cur[:])
                return

            for i in range(index, n + 1):
                cur.append(i)
                dfs(cur, i + 1)
                cur.pop()

        dfs([], 1)

        return combinations