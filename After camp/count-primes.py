class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
            
        isPrime = [True for i in range(n + 1)]
        isPrime[0] = isPrime[1] = False
        i = 2
        numberOfPrimes = 0

        while i * i <= n:
            if isPrime[i]:
                j = i * i

                while j <= n:
                    isPrime[j] = False
                    j += i

            i += 1

        for i in range(n):
            if isPrime[i]:
                numberOfPrimes += 1

        return numberOfPrimes

        

        