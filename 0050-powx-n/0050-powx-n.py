class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        powResult = defaultdict(int)
        def helper(x, n):
            if n in powResult:
                return powResult[n]
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1 / x
            
            if n % 2 == 0:
                l, r = n // 2, n // 2
            else:
                l, r = n // 2, (n // 2 + 1)
            result = helper(x, l) * helper(x, r)
            powResult[n] = result

            return result
            
        return helper(x, n)