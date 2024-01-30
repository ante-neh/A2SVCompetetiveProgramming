class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []
        maxXor = 0

        def backtrack(cur, start):
            if start > len(nums):
                return

            subsets.append(cur[:])

            for i in range(start,len(nums)):
                cur.append(nums[i])
                backtrack(cur, i + 1)
                cur.pop()


        backtrack([], 0)

        for subset in subsets:
            cur = 0
            for num in subset:
                cur |= num

            maxXor = max(maxXor, cur)

        count = 0

        for subset in subsets:
            cur = 0
            for num in subset:
                cur |= num
            
            if cur == maxXor:
                count += 1

        return count
