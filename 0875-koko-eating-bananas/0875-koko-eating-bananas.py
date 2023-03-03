class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            totalHour = 0
            for pile in piles:
                totalHour += math.ceil(pile / speed)
                
            return totalHour
        
        
        left, right = 0, max(piles) + 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if feasible(mid) > h:
                left = mid
            else:
                right = mid
                
        return right