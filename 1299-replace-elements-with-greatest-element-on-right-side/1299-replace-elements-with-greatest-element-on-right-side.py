class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
            rightMax = -1
            
            for i in range(len(arr), 0, -1):
                arr[i - 1], rightMax = rightMax, max(arr[i - 1], rightMax)
                
            return arr