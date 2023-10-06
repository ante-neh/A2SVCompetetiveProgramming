class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for city1, city2, cost in flights:
            adj_list[city1].append((cost, city2))

        heap = [(0, src, k)]
        heapify(heap)
        visited = set()
        while heap:
            cost, node, curr_k = heappop(heap)
            if (node, cost) in visited:
                continue
            visited.add((node, cost))

            if node == dst:
                return cost
            
            for nei_cost, nei in adj_list[node]:
                nei_k = k if nei == dst else curr_k - 1 
                if nei_k > -1:
                    heappush(heap, (cost + nei_cost, nei, nei_k))

        return -1