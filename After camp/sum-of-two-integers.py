class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a >= 0 else -1

        if a * b >= 0:
            while y:
                curAnswer = (x ^ y)
                carry = (x & y) << 1
                x, y = curAnswer, carry

        else:
            while y:
                curAnswer = (x ^ y)
                borrow = (~(x) & y) << 1
                x, y = curAnswer, borrow

        return x * sign
        