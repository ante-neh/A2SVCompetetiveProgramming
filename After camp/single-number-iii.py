class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        totalXor = 0

        for num in nums:
            totalXor ^= num

        diff = totalXor & (-totalXor) # extracts the last difference bit between the two numbers
        num1 = 0

        for num in nums:
            if diff & num:
                num1 ^= num

        return [num1, totalXor ^ num1]