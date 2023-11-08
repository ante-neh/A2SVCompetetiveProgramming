class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largestRectangle = 0

        for index, height in enumerate(heights):
            startIndex = index

            while stack and stack[-1][0] > height:
                val, startIndex = stack.pop()
                largestRectangle = max(largestRectangle, val * (index - startIndex))

            stack.append([height, startIndex])

        for height, index in stack:
            largestRectangle = max(largestRectangle, height * (len(heights) - index))

        return largestRectangle
                