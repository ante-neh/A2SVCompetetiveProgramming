class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def backtrack(nums, s):
            if len(nums) == k:
                combinations.append(nums.copy())
                return
            
            for i in range(s, n + 1):
                nums.append(i)
                backtrack(nums, i + 1)
                nums.pop()
                
        backtrack([], 1)
        
        return combinations