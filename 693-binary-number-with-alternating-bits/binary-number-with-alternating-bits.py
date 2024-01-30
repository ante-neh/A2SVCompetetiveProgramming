class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        stack = [n & 1]
        n >>= 1

        while n:
            cur = n & 1
            if cur == stack[-1]:
                return False
            stack.append(cur)
            n >>= 1

        return True
