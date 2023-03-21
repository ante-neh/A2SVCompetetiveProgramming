class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(seen, remaining):
            if not remaining:
                return True
            
            for index, num in enumerate(remaining):
                newSeen = seen + [num]
                
                if backtrack(newSeen,remaining[:index] + remaining[index + 1:]):
                    res.append(newSeen)
                    
            return False
        
        backtrack([], nums)
        ans = []
        
        for result in res:
            if not result in ans:
                ans.append(result)
                
        return ans