class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                curString = []
                while stack and stack[-1] != '(':
                    curString.append(stack.pop())

                stack.pop()
                stack.extend(curString)
                
            else:
                stack.append(c)

        return "".join(stack)