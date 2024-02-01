class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            
            return gcd(b, a % b)

        count = 0

        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = gcd(max(cur, nums[j]), min(cur, nums[j]))
                if cur == k:
                    count += 1

        return count
                    

            
            

        