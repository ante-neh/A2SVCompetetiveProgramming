class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)
        
        for i in range(len(nums)):
            start = nums[i]
            for j in range(i , len(nums)):
                start = gcd(max(start, nums[j]), min(start, nums[j]))
                if start == k:
                    count += 1
                    
        return count
                
                