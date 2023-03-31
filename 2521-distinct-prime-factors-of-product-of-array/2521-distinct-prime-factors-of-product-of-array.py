class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactors = []
        for num in nums:
            i = 2
            while i * i <= num:
                while num % i == 0:
                    primeFactors.append(i)
                    num //= i

                i += 1

            if num > 1:
                primeFactors.append(num)
                
            
            
        return len(set(primeFactors))