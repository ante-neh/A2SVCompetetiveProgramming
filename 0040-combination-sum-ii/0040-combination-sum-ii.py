class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(cur, indx, curSum):
            if curSum == target:
                res.append(cur[:])
                return
                
            if indx == len(candidates) or curSum > target:
                return
            
            cur.append(candidates[indx])
            backtrack(cur, indx + 1, curSum + candidates[indx])
            cur.pop()
            while indx + 1 < len(candidates) and candidates[indx] == candidates[indx + 1]:
                indx += 1
                
            backtrack(cur, indx + 1, curSum)
            
        backtrack([], 0, 0)
        
        return res
                