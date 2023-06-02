class Solution:
    def __init__(self):
        self.cache = {}
    def priceAtSpot(self, triangle, r, c):
        if ((r,c) in self.cache):
            return self.cache[(r,c)]
        if r == len(triangle)-1:
            return triangle[r][c]
        
        self.cache[(r,c)] = triangle[r][c]+min(self.priceAtSpot(triangle, r+1,c), self.priceAtSpot(triangle, r+1, c+1))
        return self.cache[(r,c)]
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.priceAtSpot(triangle, 0,0)
        
        