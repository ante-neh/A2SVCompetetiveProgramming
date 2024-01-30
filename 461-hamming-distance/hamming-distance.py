class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        while x or y:
            bit1, bit2 = x & 1, y & 1
            if bit1 and not bit2:
                distance += 1
            if not bit1 and bit2:
                distance += 1
            x >>= 1
            y >>= 1

        return distance