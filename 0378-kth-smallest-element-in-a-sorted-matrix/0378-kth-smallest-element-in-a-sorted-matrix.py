class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heappush(heap, matrix[r][c])
                
        kthSmallest = 0
        
        for i in range(k):
            kthSmallest = heappop(heap)
            
        return kthSmallest