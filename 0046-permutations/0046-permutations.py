class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(seen, available):
            if not available:
                return True
            
            for index, num in enumerate(available):
                newSeen = seen + [num]
                if backtrack(newSeen, available[:index] + available[index + 1:]):
                    res.append(newSeen)
                
            return False
        
        backtrack([], nums)
        
        return res