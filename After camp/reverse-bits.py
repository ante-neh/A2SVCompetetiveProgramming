class Solution:
    def reverseBits(self, n: int) -> int:
        result = []
        num = 0

        for i in range(32):
            result.append(n & 1)
            n >>= 1


        result = result[::-1]

        for i in range(32):
            num += (2 ** i) * result[i]


        return num