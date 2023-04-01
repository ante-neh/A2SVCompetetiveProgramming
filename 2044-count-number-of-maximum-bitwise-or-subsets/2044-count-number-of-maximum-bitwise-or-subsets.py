class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = nums[0]
        count = 0
        for i in range(1,len(nums)):
            maxOr |= nums[i]
            
        subSets = []
        def backtrack(cur, i):
            if i >= len(nums):
                if not len(cur) == 0:
                    subSets.append(cur[:])
                    
                return 
            
            cur.append(nums[i])
            backtrack(cur, i + 1)
            cur.pop()
            backtrack(cur, i + 1)
            
        backtrack([], 0)
        
        for subset in subSets:
            cur = subset[0]
            for i in range(1,len(subset)):
                cur |= subset[i]
                
            if cur == maxOr:
                count += 1
                
        return count
            