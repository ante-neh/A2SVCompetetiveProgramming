class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = -1, len(nums)
        
        while high > low + 1:
            mid = low + (high - low) // 2
            
            if nums[mid] < target:
                low = mid
            else:
                high = mid
                
        return high