class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: 
            return []
        size = [1 for i in range(len(nums))]
        prev = [i for i in range(len(nums))]
        nums.sort()
        bt = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and size[j] + 1 > size[i]:
                    size[i] = size[j] + 1
                    prev[i] = j
            if size[i] > size[bt]:
                bt = i
        ans = []
        while prev[bt] != bt:
            ans.append(nums[bt])
            bt = prev[bt]
        ans.append(nums[bt])
        return ans