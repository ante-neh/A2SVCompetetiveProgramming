class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
            
        heapify(nums)        
        kthNum = 0
        
        for i in range(k):
            kthNum = heappop(nums)
            
        return kthNum * -1
        