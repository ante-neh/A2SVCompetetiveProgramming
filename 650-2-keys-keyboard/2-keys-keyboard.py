class Solution:
    def minSteps(self, n: int) -> int:
        minNumberOfOperations = 0

        d = 2

        while d * d <= n:
            while n % d == 0:
                minNumberOfOperations +=  d
                n //= d

            d += 1
        if n > 1:
            minNumberOfOperations += n
            
        return minNumberOfOperations
            