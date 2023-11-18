class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(i, cur, prev):
            if i > len(candidates):               
                return 

            if sum(cur) >= target:
                if sum(cur) == target:
                    combinations.append(cur[:])
                    
                return 

            for j in range(i, len(candidates)):
                if candidates[j] != prev:
                    cur.append(candidates[j])
                    backtrack(j + 1, cur, prev)
                    prev = cur.pop()

        backtrack(0, [], 0)

        return combinations 