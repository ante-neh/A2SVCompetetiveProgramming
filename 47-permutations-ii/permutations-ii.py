class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        numsCount = defaultdict(int)
        permutations = []
        cur = []

        for num in nums:
            numsCount[num] += 1

        
        def backtrack():
            if len(cur) == len(nums):
                permutations.append(cur[:])
                return 

            for num in numsCount:
                if numsCount[num] > 0:
                    cur.append(num)
                    numsCount[num] -= 1
                    backtrack()
                    numsCount[num] += 1
                    cur.pop()

        backtrack()

        return permutations 
