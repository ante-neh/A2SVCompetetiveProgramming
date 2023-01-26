class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        l = 0
        
        while l < len(arr) - 1:
            if arr[l] < arr[l + 1]:
                l += 1
            else:
                break
                
        r = len(arr) - 1
        
        while r > 0:
            if arr[r - 1] > arr[r]:
                r -= 1
            else:
                break
                
        if l != (len(arr) - 1) and r != 0 and r == l:
            return True
        else:
            False