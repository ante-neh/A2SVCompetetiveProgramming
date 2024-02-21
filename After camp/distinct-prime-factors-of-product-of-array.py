class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num

        factors = []
        d = 2

        while d * d <= product:
            while not product % d:
                factors.append(d)
                product //= d

            d += 1

        if product > 1:
            factors.append(product)

        return len(Counter(factors))