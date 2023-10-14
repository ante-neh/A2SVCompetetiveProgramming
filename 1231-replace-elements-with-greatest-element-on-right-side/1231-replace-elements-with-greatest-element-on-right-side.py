class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightGreatest = -1
        
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            arr[i] = rightGreatest
            rightGreatest = max(cur, rightGreatest)

        return arr
