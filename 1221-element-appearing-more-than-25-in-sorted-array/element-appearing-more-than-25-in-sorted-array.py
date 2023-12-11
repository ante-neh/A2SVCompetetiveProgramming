class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        left = 0

        for right in range(len(arr)):
            if arr[right] != arr[left]:
                if (right - left) / len(arr) > 0.25:
                    return arr[left]
                
                left = right

        return arr[left]

            