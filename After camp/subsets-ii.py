class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def backtrack(i, cur,  prev):
            if i > len(nums):
                return

            subsets.append(cur[:])

            for j in range(i, len(nums)):
                if nums[j] != prev:
                    cur.append(nums[j])
                    backtrack(j + 1, cur, prev)
                    prev = cur.pop()

        backtrack(0, [], -11)

        return subsets