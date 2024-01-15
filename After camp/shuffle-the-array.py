class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        p1, p2 = 0, n

        while p1 < n and p2 < len(nums):
            shuffled.append(nums[p1])
            shuffled.append(nums[p2])
            p1, p2 = p1 + 1, p2 + 1

        return shuffled