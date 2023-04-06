class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start, destination = set(), set()
        
        for edge in edges:
            start.add(edge[0])
            destination.add(edge[1])
            
        res = list(start.difference(destination))
                        
        return res