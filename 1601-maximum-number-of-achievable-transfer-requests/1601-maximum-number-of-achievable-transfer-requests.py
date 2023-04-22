class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def dfs(i):
            if i == len(requests):
                return 0 if min(ans) == max(ans) == 0 else float("-inf")

            v, w = requests[i]

            ans[v] -= 1
            ans[w] += 1
            res = 1 + dfs(i+1)
            ans[v] += 1
            ans[w] -= 1

            return max(res,dfs(i+1))

        ans = [0]*n 

        return dfs(0)