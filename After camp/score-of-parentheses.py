class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)

            else:
                top = stack.pop()
                if top == 0:
                    top = 1
                
                else:
                    top *= 2

                stack[-1] += top

        return stack[0]