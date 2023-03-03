class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            total = 0
            day = 1
            
            for weight in weights:
                total += weight
                
                if total > capacity:
                    total = weight
                    day += 1
                    if day > days:
                        return False
                    
            return True
        
        left, right = max(weights) - 1, sum(weights) + 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if not feasible(mid):
                left = mid
            
            else:
                right = mid
                
        return right