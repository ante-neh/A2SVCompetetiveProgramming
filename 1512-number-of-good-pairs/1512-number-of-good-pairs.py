class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numsFreq = {}
        
        for i in range(len(nums)):
            numsFreq[nums[i]] = 1 + numsFreq.get(nums[i], 0)
            
        
            
        count = 0
        
        for item in numsFreq.items():
            curFreq = item[1]
            count += (curFreq * (curFreq - 1)) // 2
        return count 