class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curNums, index):
            if index >= len(nums):
                result.append(curNums[::])
                return 
            
            curNums.append(nums[index])
            backtrack(curNums, index + 1)
            curNums.pop()
            backtrack(curNums, index + 1)

        backtrack([], 0)

        return result