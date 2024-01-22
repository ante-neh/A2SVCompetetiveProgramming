class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1 << 31
        reversedBits = 0

        for i in range(32):
            if n & 1:
                reversedBits |= mask

            n >>= 1
            mask >>= 1

        return reversedBits