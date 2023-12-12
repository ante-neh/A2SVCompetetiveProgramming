class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstMax, secondMax = 0, 0
        ind = 0

        for index, val in enumerate(nums):
            if firstMax <= val:
                firstMax = val
                ind = index

        for index, val in enumerate(nums):
            if index != ind:
                secondMax = max(secondMax, val)

        return (secondMax - 1) * (firstMax - 1)