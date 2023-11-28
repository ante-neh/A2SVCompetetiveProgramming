class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = a * bc // gcd(a, bc)

        def isValid(mid):
            count = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            return count >= n

        left, right = min(a, b, c) - 1, 10 ** 10

        while left + 1 < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid

            else:
                left = mid


        return left + 1 