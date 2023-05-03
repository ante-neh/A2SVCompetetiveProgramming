class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:            
        heapify(nums)        
        kthNum = 0
        
        for i in range(len(nums) - k + 1):
            kthNum = heappop(nums)
            
        return kthNum
        