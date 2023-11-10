class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opening = 0
        stack = []
        result = []

        for c in s:
            if c == '(':
                opening += 1

            elif c == ')':
                if not opening:
                    continue

                opening -= 1

            stack.append(c)

        for c in reversed(stack):
            if c == '(' and opening:
                opening -= 1
                continue

            result.append(c)

        return result[::-1]
        
            