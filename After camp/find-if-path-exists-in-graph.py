class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True

            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)