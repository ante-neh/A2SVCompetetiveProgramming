class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstPos, lastPos = -1, -1
        
        left, right = -1, len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
                
        if right != len(nums) and nums[right] == target:
            firstPos = right
            
        left, right = -1, len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
                
            else:
                right = mid
                
        if left != -1 and nums[left] == target:
            lastPos = left
            
        return [firstPos, lastPos]
                
        

            