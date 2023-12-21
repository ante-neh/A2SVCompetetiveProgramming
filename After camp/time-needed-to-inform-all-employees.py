class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        timeNeeded = 0

        for i in range(len(manager)):
            graph[manager[i]].append(i)

        def dfs(node, time):
            nonlocal timeNeeded
            if graph[node] == 0:
                return
            
            timeNeeded = max(timeNeeded, time)
            
            for child in graph[node]:
                dfs(child, time + informTime[node])

        dfs(headID, 0)

        return timeNeeded 
