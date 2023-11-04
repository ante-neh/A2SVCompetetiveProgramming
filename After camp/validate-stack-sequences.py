class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushIndex, popIndex = 0, 0

        while pushIndex < len(pushed):
            stack.append(pushed[pushIndex])
            while stack and stack[-1] == popped[popIndex]:
                stack.pop()
                popIndex += 1

            pushIndex += 1

        return len(stack) == 0