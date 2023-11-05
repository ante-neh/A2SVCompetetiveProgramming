class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                curString, count = "", ""

                while stack and stack[-1] != '[':
                    curString = stack.pop() + curString

                stack.pop()

                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                stack.append(int(count) * curString)

            else:
                stack.append(c)


        return "".join(stack)