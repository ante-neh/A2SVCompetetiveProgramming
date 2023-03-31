class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        isPrime = [True for _ in range(0,n)]
        isPrime[0] = isPrime[1] = False
        i = 2
        
        while i * i < n:
            if isPrime[i]:
                j = i * i
                
                while j < n:
                    isPrime[j] = False
                    j += i
                    
            i += 1
            
        count = 0
        
        for i in range(n):
            if isPrime[i]:
                count += 1
                
        return count