class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curSum = 0
        sumFreq = {0:1}
        count = 0
        
        for num in nums:
            curSum += num
            diff = curSum - goal
            
            if diff in sumFreq:
                count += sumFreq[diff]
                
            sumFreq[curSum] = 1 + sumFreq.get(curSum, 0)
            
        return count 