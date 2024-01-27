class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0

        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1

            if count % 3:
                single |= (1 << i)


        if single & (1 << 31):
            if single > 2 ** 31:
                single = ~(single - 1) % 2 ** 31

            single *= -1

        return single