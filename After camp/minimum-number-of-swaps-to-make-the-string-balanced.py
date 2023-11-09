class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for c in s:
            if not stack or c == '[':
                stack.append(c)

            else:
                stack.pop()

        return (len(stack) + 1) // 2