class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)

        while b > 0:
            temp = a % b
            a = b 
            b = temp

        return a