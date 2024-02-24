class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 1

        while right > left:
            right &= ~(shift)
            shift <<= 1

        return right
