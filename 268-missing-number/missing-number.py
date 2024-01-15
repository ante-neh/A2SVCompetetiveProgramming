class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for index,  num in enumerate(nums):
            xor ^= (num ^ index) 

        return xor