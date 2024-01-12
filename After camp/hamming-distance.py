class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        while x != y:
            if x & 1 != y & 1:
                distance += 1

            x >>= 1
            y >>= 1

        return distance