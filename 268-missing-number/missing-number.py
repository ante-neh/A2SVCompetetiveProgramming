class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for num in nums:
            xor ^= num

        for i in range(len(nums)):
            xor ^= i

        return xor