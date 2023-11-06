class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            if k > 0:
                while stack and stack[-1] > c and k > 0:
                    stack.pop()
                    k -= 1

                stack.append(c)

            else:
                stack.append(c)

        while k > 0:
            stack.pop()
            k -= 1

        stack = "".join(stack)

        if len(stack) > 1:
            stack = stack.lstrip('0')

        return stack if stack else "0"