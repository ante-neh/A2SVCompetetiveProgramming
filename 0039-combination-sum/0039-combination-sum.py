class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(cur, i, curSum):
            if curSum == target:
                res.append(cur[:])
                return 
            
            if i == len(candidates) or curSum > target:
                return
            
            cur.append(candidates[i])
            backtrack(cur, i, curSum + candidates[i])
            cur.pop()
            backtrack(cur, i + 1, curSum)
            
        backtrack([], 0, 0)
        
        return res
                