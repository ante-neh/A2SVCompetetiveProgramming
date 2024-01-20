class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        subarrayMinimumsSum = 0
        arr.append(0)

        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                curIndex = stack.pop()
                leftIndex = stack[-1]
                subarrayMinimumsSum += arr[curIndex] * (curIndex - leftIndex) * (i - curIndex)

            stack.append(i)

        return subarrayMinimumsSum % (10**9 + 7)