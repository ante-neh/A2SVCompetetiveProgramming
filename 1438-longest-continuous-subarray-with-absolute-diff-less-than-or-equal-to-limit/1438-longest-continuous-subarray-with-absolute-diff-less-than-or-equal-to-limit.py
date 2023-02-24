class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen = 0
        left = 0
        maxQueue = []
        minQueue = []
        def good():
            return maxQueue[0] - minQueue[0] <= limit
        
            
        def remove(index):
            curr = nums[index]
            
            if maxQueue and maxQueue[0] == curr:
                maxQueue.pop(0)
                
            if minQueue and minQueue[0] == curr:
                minQueue.pop(0)
                
                
        
        for right in range(len(nums)):
            while maxQueue and maxQueue[-1] < nums[right]:
                maxQueue.pop()
                
            maxQueue.append(nums[right])
            
            while minQueue and minQueue[-1] > nums[right]:
                minQueue.pop()
                
            minQueue.append(nums[right])
            
            while not good():
                remove(left)
                left += 1
                
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
            
        
        
        
        
        