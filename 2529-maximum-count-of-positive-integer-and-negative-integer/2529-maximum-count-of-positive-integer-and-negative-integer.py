class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCount, negCount = 0, 0
        
        for num in nums:
            if num > 0:
                posCount += 1
            
            if num < 0:
                negCount += 1
                
        return max(negCount, posCount)