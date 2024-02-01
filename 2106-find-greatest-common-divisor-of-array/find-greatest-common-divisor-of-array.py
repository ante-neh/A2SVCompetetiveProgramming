class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)

        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)

        return gcd(a, b)