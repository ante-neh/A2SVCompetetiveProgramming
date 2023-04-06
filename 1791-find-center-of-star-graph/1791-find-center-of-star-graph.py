class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertixCount = {}
        
        for r in range(len(edges)):
            for c in range(len(edges[0])):
                vertixCount[edges[r][c]] = 1 + vertixCount.get(edges[r][c], 0)
                
            
        for items in vertixCount.items():
            if items[1] > 1:
                return items[0]