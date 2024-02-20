class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        numberOfSubarrays = 0

        for i in range(len(nums)):
            curGcd = nums[i]
            for j in range(i, len(nums)):
                curGcd = self.gcd(max(curGcd, nums[j]), min(curGcd, nums[j]))
                if curGcd == k:
                    numberOfSubarrays += 1
                

        return numberOfSubarrays


    def gcd(self, a, b):
        if b == 0:
            return a
        
        return gcd(b, a % b)