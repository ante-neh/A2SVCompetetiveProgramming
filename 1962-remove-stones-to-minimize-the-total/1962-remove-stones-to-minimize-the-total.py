class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:        
        for i in range(len(piles)):
            piles[i] *= -1  
        heapify(piles)
        for i in range(k):
            maxValue = heappop(piles)
            maxValue -= ceil(maxValue / 2)
            heappush(piles, maxValue)
            
        return -1 * sum(piles)