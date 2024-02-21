class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True for i in range(right + 1)]
        if right <= 1:
            return [-1, -1]

        isPrime[0] = isPrime[1] = False
        i = 2

        while i * i <= right:
            if isPrime[i]:
                j = i * i
                while j <= right:
                    isPrime[j] = False
                    j += i

            i += 1

        validPrimes = []
        minDiff = float("inf")
        result = [-1, -1]

        for i in range(left, len(isPrime)):
            if isPrime[i]:
                validPrimes.append(i)

        for i in range(1, len(validPrimes)):
            if validPrimes[i] - validPrimes[i - 1] < minDiff:
                minDiff = validPrimes[i] - validPrimes[i - 1]
                result[0] = validPrimes[i - 1]
                result[1] = validPrimes[i]

        return result
        


