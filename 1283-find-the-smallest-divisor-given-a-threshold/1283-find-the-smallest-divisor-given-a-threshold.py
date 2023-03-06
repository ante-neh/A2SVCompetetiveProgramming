class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(val):
            total = 0
            
            for num in nums:
                total += math.ceil(num / val)
                
            return total <= threshold
        
        left, right = 0, sum(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if not condition(mid):
                left = mid
                
            else:
                right = mid
                
        
        return right