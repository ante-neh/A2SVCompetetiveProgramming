class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = 0
        
        while l < len(arr) - 1 and arr[l] < arr[l + 1]:
            l += 1
            
        r = len(arr) - 1
        
        while r > 0 and arr[r - 1] > arr[r]:
            r -= 1
                
        return l != (len(arr) - 1) and r != 0 and l == r