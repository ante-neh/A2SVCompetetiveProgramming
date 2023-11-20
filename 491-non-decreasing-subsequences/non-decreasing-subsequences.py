class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subSequences = set()

        def backtrack(cur, index):
            if index > len(nums):
                return

            if len(cur) >= 2:
                subSequences.add(tuple(cur[:]))

            for i in range(index, len(nums)):                                       
                if not cur or (cur and cur[-1] <= nums[i]):
                    cur.append(nums[i])
                    backtrack(cur, i + 1)
                    cur.pop()

                

        backtrack([], 0)
        
        return subSequences

