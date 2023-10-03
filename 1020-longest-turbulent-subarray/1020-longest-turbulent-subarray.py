class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        sign = ""
        maxLength = 1
        left = 0
        right = 1

        while right < len(arr):
            if arr[right - 1] > arr[right] and sign != '>':
                maxLength = max(maxLength, right - left + 1)
                right += 1
                sign = '>'
            
            elif arr[right - 1] < arr[right] and sign != '<':
                maxLength = max(maxLength, right - left + 1)
                right += 1
                sign = '<'
            else:
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                sign = ""

        return maxLength


