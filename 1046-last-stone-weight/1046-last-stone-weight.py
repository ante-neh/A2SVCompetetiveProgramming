class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1* stones[i]
        heapify(stones)
        while len(stones) != 1:
            val1 = abs(heappop(stones))
            val2 = abs(heappop(stones))
            heappush(stones, -1 *(val1 - val2))
            
        return -1 * stones[0]
        
        