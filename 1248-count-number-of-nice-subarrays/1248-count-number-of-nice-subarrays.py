class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        sumCount = {0:1}
        curSum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            
            else:
                nums[i] = 1
        
        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            
            if diff in sumCount:
                count += sumCount[diff]
                
            sumCount[curSum] = 1 + sumCount.get(curSum, 0)
            
        return count