class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subSets = []
        
        def backtrack(cur, i):
            if i >= len(nums):
                subSets.append(cur[:])
                return 
            
            cur.append(nums[i])
            # decision to include
            backtrack(cur, i + 1)
            cur.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # decision not to include
            backtrack(cur, i + 1)
            
        backtrack([], 0)
        
        return subSets