class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        open, close = 0, 0
        result = ""
        for c in s:
            if c == '(':
                open += 1
            elif c == ')':
                close += 1

            if  c == ')' and open == close:
                result += "".join(stack[1:])
                stack = []
                close = open = 0
            else:
                stack.append(c)

        return result

            