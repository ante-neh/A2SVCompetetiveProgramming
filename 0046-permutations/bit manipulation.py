class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, curr = [], []
        used = 0

        def build(i=0):
            nonlocal used
            if i == len(nums):
                ans.append(curr.copy())
                return

            for idx, num in enumerate(nums):
                if (used & (1 << idx)) == 0:
                    used |= 1 << idx
                    curr.append(num)
                    build(i+1)
                    curr.pop()
                    used ^= 1 << idx
        build()
        return ans
    # bit manipulation