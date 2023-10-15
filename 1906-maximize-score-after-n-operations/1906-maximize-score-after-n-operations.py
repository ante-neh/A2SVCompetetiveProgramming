from math import gcd 
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def rec(ops , cur_nums):

            res =0
            for i in range(len(cur_nums)):
                for j in range(i+1 ,len(cur_nums)):
                    new_nums = cur_nums[:i] + cur_nums[i+1:j] +cur_nums[j+1:]

                    res = max(
                        res , 
                        ops * gcd(cur_nums[i] , cur_nums[j]) + rec(ops+1 , new_nums)
                    )

            return res
        
        return rec(1 , tuple(nums))
        
