class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remCount = {0:1}
        count = 0
        curSum = 0
        
        for num in nums:
            curSum += num
            quet = curSum % k
            if quet in remCount:
                count += remCount[quet]
            
            remCount[quet] = 1 + remCount.get(quet, 0)
            
        return count