class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dagGraph = defaultdict(list)
        count = 0
        target = len(graph) - 1
        res = []
        
        for r in range(len(graph)):
            for c in range(len(graph[r])):
                dagGraph[r].append(graph[r][c])
                
        def dfs(node, cur):
            if node == target:
                res.append(cur[:])
                return
            
            for neighbour in dagGraph[node]:
                cur.append(neighbour)
                dfs(neighbour, cur)
                cur.pop()
                    
            return 
        
        dfs(0, [0])
        
        return res
                    
                    
            