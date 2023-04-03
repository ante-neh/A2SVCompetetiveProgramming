class Solution:
    def minSteps(self, n: int) -> int:
        primeFactors = {}
        minNumOperations = 0
        i = 2
        # finding the prime factors of n
        while i * i <= n:
            while n % i == 0:
                primeFactors[i] = 1 + primeFactors.get(i, 0)
                n //= i
                
            i += 1
        # check if the remaining number is prime
        if n > 1:
            primeFactors[n] = 1 + primeFactors.get(n, 0)
        
        # calculate how many minimum number of operations required
        for item in primeFactors.items():
            minNumOperations += item[0] * item[1]
            
        return minNumOperations
            