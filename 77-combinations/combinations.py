class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(i, cur):
            if len(cur) >= k:
                combinations.append(cur[:])
                return

            for i in range(i, n + 1):
                cur.append(i)
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(1, [])

        return combinations