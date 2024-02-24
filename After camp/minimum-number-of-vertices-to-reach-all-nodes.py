class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        visited = set()
        vertices = set()
        for u, v in edges:
            visited.add(v)

        for u, v in edges:
            if not u in visited:
                vertices.add(u)

        return vertices
        
