class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(n):
            if n == 0:
                return 1
            if n == 1 :
                return x

            half = calculate(n // 2)
            if n % 2 == 1:
                return half * half * x

            else:
                return half * half

        if n < 0:
            return 1 / calculate(-1 * n)

        return calculate(n)