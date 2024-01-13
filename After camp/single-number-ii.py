class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0

        for shift in range(32):
            count = 0
            for num in nums:
                count += (num >> shift) & 1

            if count % 3 != 0:
                single |= (count % 3 << shift)

        if single >= 1 << 31:
            single = (2 ** 32 - single) * -1

        return single
            
