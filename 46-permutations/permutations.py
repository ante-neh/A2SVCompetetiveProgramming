class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = 0
        permutations = []

        def backtrack(cur):
            nonlocal visited
            if len(cur) == len(nums):
                permutations.append(cur[:])
                return

            for index, num in enumerate(nums):
                if visited & (1 << index) == 0:
                    visited |= (1 << index)
                    cur.append(num)
                    backtrack(cur)
                    cur.pop()
                    visited ^= (1 << index)
        
        backtrack([])

        return permutations