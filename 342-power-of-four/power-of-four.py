class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n % 3 == 1 if n > 0 else False