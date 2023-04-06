class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for i in range(n)]
        maximalNetworkRank = 0
        
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
            
        for i in range(len(graph) - 1):
            for j in range(i+1, len(graph)):
                if i in graph[j]:
                    maximalNetworkRank = max(maximalNetworkRank, len(graph[i]) + len(graph[j]) - 1)
                else:
                    maximalNetworkRank = max(maximalNetworkRank, len(graph[i]) + len(graph[j]))
                    
        return maximalNetworkRank
                    
            