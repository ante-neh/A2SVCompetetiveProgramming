class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree =[0 for _ in range(numCourses)]
        order = []
        graph = defaultdict(list)
        queue = deque()
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
            
        for i, count in enumerate(indegree):
            if count == 0:
                queue.append(i)
                
            
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return len(order) == numCourses
                    
            
        