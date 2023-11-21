class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        def backtrack(index):
            if index >= len(requests):
                return 0 if min(indegree) == max(indegree) else float("-inf")

            start, end = requests[index]
            indegree[start] -= 1
            indegree[end] += 1
            res = 1 + backtrack(index + 1)
            indegree[start] += 1
            indegree[end] -= 1

            return max(res, backtrack(index + 1))

        return backtrack(0)