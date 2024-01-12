class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        leftShiftCount = 0

        while left != right:
            left >>= 1
            right >>= 1
            leftShiftCount += 1

        return left << leftShiftCount